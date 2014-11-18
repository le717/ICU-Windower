# ICU Logging code
# https://github.com/le717/ICU
# Copyright 2013 Triangle717 (http://triangle717.wordpress.com)

# logging.BasicConfig code based on example from 'A Byte of Python'
# http://www.swaroopch.com/notes/Python

import os, logging, time, winreg

# ------------ Begin ICU Logging Code ------------ #


def appLoggingFolder():
    '''Checks for (and creates) ICU Logs folder'''

    try:
        # The Logs folder does not exist in the current directory
        if not os.path.exists(os.path.join(os.getcwd(), "Logs")):
            # Create the Logs folder
            logsfolder = os.mkdir(os.path.join(os.getcwd(), "Logs"))

    # User does not have Admin rights
    except PermissionError:
        print("\nICU Windower does not have the user rights to operate!\nPlease relaunch ICU Windower as an Administrator.")
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit


# AKA if this is imported as a module
if "__main__" != __name__:
    appLoggingFolder()

    # -- Begin Logging Config -- #

    logging_file = os.path.join(os.getcwd(), "Logs", 'YourScoreCube.log')

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s : %(levelname)s : %(message)s",
        filename = logging_file,
        filemode = 'a+',
    )

    # -- End Logging Config -- #

# ------------ End ICU Logging Code ------------ #
