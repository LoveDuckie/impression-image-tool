import json, os, sys
from typing import Any

class Configuration:
    def __init__(self, *args, **kwargs) -> None:
        pass
    
    def __getattribute__(self, __name: str) -> Any:
        if __name is None:
            raise Exception("The name for the attribute is invalid or null")
        pass
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name is None:
            raise Exception("The name for the attribute is invalid or null")
        pass
    
    def __str__(self) -> str:
        pass
    
    @classmethod()
    def load_config(config_file_path: str):
        return
    
    
    def save_config(self, config_file_path: str = None):
        if config_file_path is None:
            raise Exception("The absolute path to the configuration file is invalid or null")
        
        serialized = json.dumps(self.__dict__)
        
        return