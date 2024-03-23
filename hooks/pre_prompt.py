import os
import subprocess
from cookiecutter.main import cookiecutter
import datetime

from utils import bcolors
    
def is_conda_installed() -> bool:
    try:
        subprocess.check_output(["conda", "--version"])
        return True
    except FileNotFoundError:
        return False
    
def check_directory_permissions() -> bool:
    # Check if the current directory is writable
    if not os.access(path=os.getcwd(), mode=os.W_OK):
        return False
    return True

def check_snakemake_installed() -> bool:
    try:
        version = subprocess.check_output(["snakemake", "--version"]).decode("utf-8").strip()
        if version >= "7.0.0":
            return True
        else:
            return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    
    # Check if the current directory is writable
    if not check_directory_permissions():
        print(f"{bcolors.FAIL}ERROR: Current directory is not writable. \
            Please change the directory or check the permissions.{bcolors.ENDC}")
        exit(1)
    
    if not is_conda_installed():
        print(
            f"""{bcolors.FAIL}ERROR: Conda is not installed.
                Please install conda before using this project.{bcolors.ENDC}""")
        exit(1)
        
    # if not check_snakemake_installed():
    #     print(f"{bcolors.FAIL}ERROR: Snakemake is not installed or the version is not compatible."
    #         f"\nPlease install snakemake >= 7.0.0 before using this project.{bcolors.ENDC}")
    #     exit(1)
    
    # print starting in okgreen
    print(f"{bcolors.OKGREEN}Starting the project build...\n{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}Separate multiple entries with a semi-colon (;).{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Values in blue are presented as default values.{bcolors.ENDC}")
    
    

    
    