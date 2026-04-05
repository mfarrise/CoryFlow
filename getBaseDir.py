import os
from pathlib import Path
import sys
def get_base_dir():

    if getattr(sys, 'frozen', False):
        BASE_DIR = Path(sys._MEIPASS)
    else:
        BASE_DIR = Path(__file__).resolve().parent

    print("base dir is : ",str(BASE_DIR)+os.sep)
    return str(BASE_DIR)+os.sep

