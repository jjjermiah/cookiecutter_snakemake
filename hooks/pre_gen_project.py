import re
import sys


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

# NAMES should be full name of the project owner(s), separated by ';'
NAMES_REGEX = r'^[a-zA-Z]+\s[a-zA-Z\s]+(;[a-zA-Z]+\s[a-zA-Z\s]+)*$'
NAME = '{{ cookiecutter.OWNER }}'

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
PROJECT_NAME = '{{ cookiecutter.Directory_Name }}'

# "EMAIL": "Email of the project owner(s), separated by ';'",
EMAIL_REGEX = r'^\S+@\S+\.\S+$'
MULTIPLE_EMAIL_REGEX = r'^\S+@\S+\.\S+(;\S+@\S+\.\S+)*$'
EMAIL = '{{ cookiecutter.EMAIL }}'

if not re.match(NAMES_REGEX, NAME):
    print(f'{bcolors.FAIL}ERROR: Names field:\n'
          f'\t{bcolors.OKCYAN}{NAME}\n'
          f'{bcolors.FAIL}is/are not valid!'
          f'Please enter the full name of the project owner(s), separated by ";"{bcolors.ENDC}')
    sys.exit(1)

if not re.match(MODULE_REGEX, PROJECT_NAME):
    print(f'{bcolors.FAIL}ERROR: {PROJECT_NAME} is not a valid Project name!{bcolors.ENDC}'
            f'\nPlease enter a valid Project name of only letters, numbers, and underscores.')
    sys.exit(1)
    
if not re.match(EMAIL_REGEX, EMAIL) or not re.match(MULTIPLE_EMAIL_REGEX, EMAIL):
    print(f'{bcolors.FAIL}ERROR: Email field: {EMAIL} is/are not valid!{bcolors.ENDC}')
    sys.exit(1)
