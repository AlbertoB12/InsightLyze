"""
# Help-utility to ensure that the user has all the needed packages (and the respective versions) installed
# If one or more packages (or versions) are missing, they will be automatically installed
"""

### Packages
from utils.helpers import Check_pip
from utils import Check_and_install_packages

### Functions
# Main function to check if pip is installed and check and install packages and versions needed for the software
def install_packages():
    # Check if pip is installed
    Check_pip.check_pip()
    # Check if needed packages and versions are installed. If not, install them
    Check_and_install_packages.check_and_install()