import os, sys
from random import choices
import logging
from logging.handlers import RotatingFileHandler
import argparse
import datetime
from PIL import Image, ImageDraw, ImageFilter
from utils import get_default_log_filename, get_default_logs_path, get_tool_name, get_default_assets_path, get_supported_social_media_platforms, log_error_exception
from configparser import ConfigParser, SafeConfigParser
from config import Configuration

if not os.path.exists(get_default_logs_path()):
    os.makedirs(get_default_logs_path())

def get_default_log_filepath() -> str:
    return os.path.join(get_default_logs_path(), get_default_log_filename())

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.Logger(name=get_tool_name(), level=logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.addHandler(RotatingFileHandler(get_default_log_filepath()))

arg_parser = argparse.ArgumentParser(description='A script responsible for generating impression images for blog posts')
arg_parser.add_argument('--languages', dest='languages', help='The list of languages to generate the impression image from', nargs="+", default=[], type=str)
arg_parser.add_argument('--language', dest='all_languages', help='The list of languages to generate the impression image from', action='append', default=[], type=str)
arg_parser.add_argument('--technologies', dest='technologies', help='The list of technologies to generate impression image from', nargs="+", default=[], type=str)
arg_parser.add_argument('--background-filepath', dest='background_filepath', help='The list of technologies to generate impression image from', default='', type=str)
arg_parser.add_argument('--assets-path', dest='assets_path', help='The absolute path to where all the assets are stored', default=get_default_assets_path(), type=str)
arg_parser.add_argument('--logs-path', dest='logs_path', help='The absolute path to where the logs are to be stored', default=get_default_logs_path(), type=str)
arg_parser.add_argument('--output-path', dest='output_path', help='The absolute path to where the logs are to be stored', default=get_default_logs_path(), type=str)
arg_parser.add_argument('--operation', dest='operation', help='Defines the type of operation to perform with the tool', default='generate', choices=['generate', 'randomize'], type=str)
arg_parser.add_argument('--padding', dest='padding', help='Specifies the amount of padding there ought to be from the edge of the background image, and the logo images themselves.', default=5, type=int)
arg_parser.add_argument('--logo-spacing', dest='logo_spacing', help='Specifies the amount of spacing there ought to be between each logo that is rendered.', default=10, type=int)
arg_parser.add_argument('--blur-background', dest='blur_background', help='Blur the background image.', default=True, type=bool)
arg_parser.add_argument('--blur-background-amount', dest='blur_background_amount', help='Blur background amount.', default=5, type=int)
arg_parser.add_argument('--use-svg', dest='use_svg', help='Attempt to use the SVG, and rasterize a custom version of the image ahead of time.', default=True, type=bool)
arg_parser.add_argument('--social-media', dest='social_media', help='The social media platforms to generate variants of the same impression image for.', nargs="+", default=get_supported_social_media_platforms(), choices=get_supported_social_media_platforms(), type=str)
parsed_args = arg_parser.parse_known_args()[0]

def get_programming_language_asset_path(language_name: str) -> str:
    if language_name is None or language_name == '':
        raise ValueError("The name of the language is invalid or empty")
    return

def get_technology_asset_path(technology_name: str) -> str:
    """Retrieve the absolute path to where the technology logo assets are located

    Args:
        technology_name (str): The name of the technology

    Raises:
        ValueError: If the name of technology is null or invalid

    Returns:
        str: The absolute path of the technology's logo assets.
    """
    if technology_name is None or technology_name == '':
        raise ValueError("The name of the technology is invalid or empty")
    return

def get_default_rasterized_logo(prefix: str, name: str) -> str:
    
    return

if parsed_args is None:
    raise Exception("The parsed arguments are invalid or null")

def main(argv):
    config_inst = Configuration.load_config("")
    if config_inst is None:
        raise ValueError("The configuration file was not loaded")
    
    logger.info(f"Assets Path: \"{parsed_args.assets_path}\"")
    logger.info(f"Background Image: \"{parsed_args.background_filepath}\"")
    logger.info(f"Languages: \"{', '.join(parsed_args.languages)}\"")
    logger.info(f"Technologies: \"{', '.join(parsed_args.technologies)}\"")
    logger.info(f"Output Path: \"{', '.join(parsed_args.output_path)}\"")

    if not os.path.exists(parsed_args.assets_path):
        logger.error(f'The path \"{parsed_args.assets_path}\" does not exist. Terminating.')
        return
    
    if not os.path.exists(parsed_args.background_filepath):
        logger.error(f'The background image \"{parsed_args.background_filepath}\" does not exist. Terminating.')
        return
    
    try:
        impression_background = Image.open(parsed_args.background_filepath)
        if impression_background is None:
            raise ValueError("The loadd impression image is invalid or null")
    except Exception as exc:
        logger.error()
    
    padding_offset = parsed_args.padding * 2
    max_image_width = impression_background.width - (padding_offset)
    max_image_height = impression_background.height - (padding_offset)
    
    if parsed_args.blur_background == True:
        impression_background = impression_background.filter(ImageFilter.GaussianBlur(parsed_args.blur_background_amount))
        
    if not any(parsed_args.technologies) and not any(parsed_args.languages):
        raise Exception("No technologies or languages were defined")
    
    total_logos = len(parsed_args.technologies) + len(parsed_args.languages)
    total_logo_spacing = parsed_args.spacing * (total_logos - 1)
    logo_max_width = (max_image_width / total_logos) - total_logo_spacing
    logo_max_height = (max_image_height / total_logos) - total_logo_spacing
        
    logo_counter = 0
    
    pos_x, pos_y = parsed_args.padding
        
    for technology in parsed_args.technologies:
        logger.debug(f"adding logo for technology \"{technology}\"")
        logo_image_filepath = get_default_rasterized_logo("Technologies", technology)
        logo_image = Image.open(logo_image_filepath)
        impression_background.paste(logo_image, (pos_x, pos_y), logo_image)
        pos_x += parsed_args.spacing
        ++logo_counter
    
    for language in parsed_args.languages:
        logger.debug(f"adding logo for programming language \"{language}\"")
        logo_image_filepath = get_default_rasterized_logo("Languages", language)
        logo_image = Image.open(logo_image_filepath)
        impression_background.paste(logo_image, (pos_x, pos_y), logo_image)
        pos_x += parsed_args.spacing
        ++logo_counter
        
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exc:
        log_error_exception(logger,exc)