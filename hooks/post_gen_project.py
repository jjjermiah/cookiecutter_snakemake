import os

PSETDIR: str = os.path.abspath(path="/home/bioinf/bhklab/psets")

# add a symbolic link to the psets directory
if(f'{{ cookiecutter.REFERENCE_DIR }}' == "True"):
    os.symlink(src=PSETDIR, dst="PSET_DIR", target_is_directory=True)
    