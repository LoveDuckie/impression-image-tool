import os, sys
from random import choices
import logging
from logging.handlers import RotatingFileHandler
import argparse
import datetime
from PIL import Image, ImageDraw, ImageFilter
from utils import get_default_log_filename, get_default_logs_path, get_tool_name, get_default_assets_path, get_supported_social_media_platforms, log_error_exception
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
arg_parser.add_argument('--padding', dest='padding', help='Specifies the amount of padding there ought to be from the edge of the background image, and the logo images themselves.', default='generate', choices=['generate','randomize'], type=str)
arg_parser.add_argument('--blur-background', dest='blur_background', help='Blur the background image.', default=True, type=bool)
arg_parser.add_argument('--blur-background-amount', dest='blur_background_amount', help='Blur background amount.', default=5, type=int)
arg_parser.add_argument('--social-media', dest='social_media', help='The social media platforms to generate variants of the same impression image for.', nargs="+", default=get_supported_social_media_platforms(), choices=get_supported_social_media_platforms(), type=str)
parsed_args = arg_parser.parse_known_args()[0]

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
    
    if parsed_args.blur_background == True:
        impression_background = impression_background.filter(ImageFilter.GaussianBlur(parsed_args.blur_background_amount))
        
    if parsed_args.technologies is None or not any(parsed_args.technologies):
        raise Exception("No technologies were specified unable to continue")
    
    if parsed_args.lanugages is None or not any(parsed_args.languages):
        raise Exception("No languages were specified unable to continue")
        
    for technology in parsed_args.technologies:
        logger.debug(f"adding logo for technology \"{technology}\"")
        pass
    
    for language in parsed_args.languages:
        logger.debug(f"adding logo for programming language \"{language}\"")
        pass
        
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exc:
        log_error_exception(logger,exc)