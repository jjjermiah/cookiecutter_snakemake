import os
import socket 

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
if(f'{{ cookiecutter.REFERENCE_DIR }}' == "True"):
    
    host = get_machine_type()
    
    if host != "labserver" and host != "h4h":
        print("This is not a lab server. Skipping symbolic link creation.")
    else:
        os.symlink(src=PSETDIR, dst="PSET_DIR", target_is_directory=True)
    