# This script is built to manage PATH of this project.
import os, sys

# Root of this project
PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH_ROOT)
print(f"Path Initialization is completed with the folder: {PATH_ROOT} ...")
