#! python3
"""
    This file is part of ICU (LEGO Island Configuration Utility)

    ICU - A collection of LEGO Island Configuration Tools
    Created 2012-2013 Triangle717 <http://triangle717.wordpress.com>

    ICU is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ICU is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ICU. If not, see <http://www.gnu.org/licenses/>.
"""
# ICU Logging code
# https://github.com/le717/ICU

# logging.BasicConfig code based on example from 'A Byte of Python'
# http://www.swaroopch.com/notes/Python

import os
import sys
import logging
import time

# Location of ICU
appFolder = os.path.dirname(sys.argv[0]).replace("/", os.path.sep)
logsFolder = os.path.join(appFolder, "Logs")
loggingFile = os.path.join(logsFolder, "Debug.log")


# ------------ Begin ICU Logging Code ------------ #

try:
    # The Logs folder does not exist in the current directory
    if not os.path.exists(logsFolder):
        # Create the Logs folder
        os.makedirs(logsFolder)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s : %(levelname)s : %(message)s",
        filename=loggingFile,
        filemode="a",
    )

    logging.info("Begin logging to {0}".format(loggingFile))

# User does not have Admin rights
except PermissionError:
    print('''
ICU does not have the required permissions to operate!
Please relaunch ICU with Administrator rights.''')

    # Display message long enough for the user to read it
    time.sleep(3)

    # Close program
    raise SystemExit(0)

# ------------ End ICU Logging Code ------------ #