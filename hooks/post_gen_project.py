import os
import socket 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def get_machine_type():
    hostname: str = socket.gethostname()
    # Add conditionals to distinguish between your server and MacBook Pro
    if "bioinformatics1" in hostname:
        return "labserver"
    elif "BHKLabs-MacBook-Pro" in hostname:
        return "local"
    elif "h4h" in hostname:
        return "h4h"
    else:
        return "Unknown"


PSETDIR: str = os.path.abspath(path="/home/bioinf/bhklab/psets")

# add a symbolic link to the psets directory
if(f'{{ cookiecutter.PSET_DIR }}' == "True"):
    
    host = get_machine_type()
    
    if host != "labserver" and host != "h4h":
        print(f"{bcolors.FAIL}This is not a lab server. Skipping symbolic link creation.{bcolors.ENDC}")
    else:
        os.symlink(src=PSETDIR, dst="PSET_DIR", target_is_directory=True)
        print(f"{bcolors.OKGREEN}Symbolic link to PSET_DIR created!{bcolors.ENDC}")
        print(f'{bcolors.OKCYAN}PSET_DIR{bcolors.OKGREEN} -> {PSETDIR}{bcolors.ENDC}')