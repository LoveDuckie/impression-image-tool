import datetime
from logging import Logger
import os
import sys


def get_tool_name():
    return 'impression-image-tool'


def get_formatted_timestamp() -> str:
    today_date = datetime.datetime.strftime(
        datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')
    if today_date is None:
        raise Exception("The formatted date string is invalid or null")
    return today_date


def get_default_log_filename() -> str:
    return f'{get_tool_name()}-log-{get_formatted_timestamp()}.log'


def get_root_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))


def get_default_config_path() -> str:
    return os.path.join(get_root_path(), ".config")


def get_default_config_filepath() -> str:
    return os.path.join(get_default_config_path(), "default.ini")


def get_default_logs_path() -> str:
    return os.path.join(get_root_path(), ".logs")


def get_supported_social_media_platforms() -> list:
    return ['linkedin', 'twitter', 'facebook', 'pinterest']


def get_default_assets_path():
    return os.path.abspath(os.path.join(get_root_path(), "..", "..", "..", "..", "Raw", "Branding"))


def get_default_technologies_assets_path(assets_path=get_default_assets_path()):
    return os.path.join(assets_path, "technologies")


def get_default_languages_assets_path(assets_path=get_default_assets_path()):
    return os.path.join(assets_path, "languages")


def generate_output_path():
    return os.path.join(get_root_path(), "output")


def generate_output_filepath():
    return os.path.join(generate_output_path(), f"impression-image-{get_formatted_timestamp()}.png")


def get_assets_path(prefix: str, name: str) -> str:
    if prefix is None or prefix == '':
        raise Exception("The prefix is invalid or null")

    if name is None or name == '':
        raise Exception("The name is invalid or null")
    return