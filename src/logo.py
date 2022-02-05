from ast import Tuple
import os, sys

class RasterizedLogo:
    def __init__(self, rasterized_logo_filepath: str) -> None:
        if rasterized_logo_filepath is None:
            raise Exception("The absolute path to the rasterized logo is invalid or null")
        if not os.path.exists(rasterized_logo_filepath):
            raise FileExistsError(f"The file \"{rasterized_logo_filepath}\" could not be found.")
        pass
    
    def resize(self, dimensions: Tuple):
        return
    
    def save(self, image_filepath: str = None):
        return
    
class VectorLogo:
    def __init__(self, vector_logo_filepath: str) -> None:
        if vector_logo_filepath is None:
            raise Exception("")
        if not os.path.exists(vector_logo_filepath):
            raise FileExistsError(f"The file \"{vector_logo_filepath}\" could not be found.")
        pass
    
    def rasterize(self, dimensions: Tuple) -> None:
        pass