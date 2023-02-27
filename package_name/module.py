import package_name as pkg
from package_name.conf import logger

def print_version():
    """Print the version of the package.
    
    This function is used to print the version of the package.

    Returns
    -------
    None
        This function does not return anything.
        
    """
    logger.info(pkg.__version__)