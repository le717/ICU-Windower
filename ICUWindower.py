#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""ICU Windower.

This file is part of ICU (LEGO Island Configuration Utility)

ICU - A collection of LEGO Island Configuration Tools
Created 2012-2014 Triangle717 <http://triangle717.wordpress.com>

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

from __future__ import print_function

import os
import sys
import time
import platform
import webbrowser
import subprocess
import logging
from tkinter import (Tk, filedialog)

from logger import iculogger  # noqa
from registry import strings

# Global constants
appName = "ICU Windower"
majVer = "Version 2.0"
minVer = ".2"
creator = "Triangle717"
game = "LEGO Island"


def preload():
    """Python 3.3 and Windows architecture checks."""
    logging.info("""
                                ###########################################
                                           {0} {1}{2}
                                        Copyright 2012-2014 {3}


                                  If you run into a bug, open an issue at
                                  https://github.com/le717/ICU/issues
                                  and attach this file for an easier fix!
                                ###########################################
                                """.format(appName, majVer, minVer, creator))

    # You need to have at least Python 3.3.0 to run ICU Windower
    if sys.version_info[:2] <= (3, 3):
        logging.warning("This is not >= Python 3.3.0!")
        print("You need Python 3.3.0 or greater to run {0} {1}{2}"
              .format(appName, majVer, minVer))

        time.sleep(4)
        webbrowser.open_new_tab("http://python.org/download")
        raise SystemExit(0)

    # This is >= Python 3.3.0
    else:
        # The user is running an unsupported version of Windows!
        if platform.machine() not in ("AMD64", "x86"):
            logging.warning("User is running an unsupported OS!")
            print("\nYou are running an unsupported OS! {0} will now close."
                  .format(appName))
            time.sleep(2)
            logging.info("{0} is shutting down".format(appName))
            raise SystemExit(0)


def main():
    """Menu Layout."""
    print("\n{0} {1}{2}\nCreated 2012-2014 {3}".format(
          appName, majVer, minVer, creator))
    print("""
Please make a selection:

[f] Full Screen Mode
[w] Windowed Mode
[q] Quit""")

    menuopt = input("\n> ")

    while True:
        if menuopt.lower() == "f":
            logging.info("User pressed '[f] Full Screen Mode'")
            fullScreenMode()

        elif menuopt.lower() == "w":
            logging.info("User pressed '[w] Windowed Mode'")
            windowedMode()

        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            raise SystemExit(0)

        else:
            logging.info("User pressed an undefined key")
            main()


def runGame():
    """Launch LEGO Island."""
    try:
        # Get location of LEGO Island
        gamePath = strings.ReadDiskPath()
        logging.info("LEGO Island Installation located at {0}".format(
            gamePath))

    # We could not find the game location
    except OSError:
        logging.warning("Cannot find LEGO Island installation!")
        print("A {1} installation could not be found!".format(game))
        time.sleep(2)

        # Ask if user wants to manually select the installation
        logging.info("Do you want to select an installation yourself?")
        print("Do you want to manually select a {0} installation?".format(
            game))
        manualSelect = input("\n\n> ")

        # Nope, go back to the menu
        if manualSelect.lower() != "y":
            main()

        # Yes, I want to select an installation
        else:
            selecttheIsland()

    # Launch LEGO Island?
    print("\nDo you want to play {0} now? {1}".format(game, r"(y\N)"))
    runGame = input("\n> ")

    # No, don't launch it
    if runGame.lower() != "y":
        logging.warning("User does not want to play LEGO Island right now!")
        main()

    # Yes, launch it (User presses 'y',
    # which is the only key that will run the game)
    else:
        try:
            # If the exe name is all uppercase, it will not load.
            # If it is all lowercase, it runs.
            # Ah, the mysteries of the Island continue...
            logging.info('Run "legoisle.exe", located at {0}'.format(gamePath))
            subprocess.call([os.path.join(gamePath, "legoisle.exe")])

            logging.info("{0} is shutting down".format(appName))
            raise SystemExit(0)

        # Cannot find exe at gamepath entered
        except OSError:
            logging.warning('Cannot find {0} installation at "{1}"!'.format(
                game, gamePath))
            print('\nCannot find {0} installation at\n"{1}"!'.format(
                  game, gamePath))
            time.sleep(3)
            main()

            # Ask if user wants to manually select the installation
            logging.info("Do you want to select an installation yourself?")
            print("Do you want to manually select a {0} installation?".format(
                game))
            manualSelect = input("\n\n> ")

            # Nope, go back to the menu
            if manualSelect.lower() != "y":
                logging.warning("Do not manually select an installation!")
                main()

            # Yes, I want to select an installation
            else:
                logging.info("Manually select an installation")
                selecttheIsland()


def windowedMode():
    """Activate LEGO Island Windowed Mode."""
    logging.info("Creating Windowed Mode registry strings")
    try:
        # Write registry strings
        strings.Write3DDeviceName("Ramp Emulation")
        strings.WriteFullScreen("NO")

        # TODO These could be the key to always activating windowed mode
        # le717/ICU@66dfd14afd3d4d0f611f7876057951f77eb6808c
        strings.WriteBuffers("NO")
        strings.WriteSurfaces("NO")

        print("\nWindowed Mode sucessfully activated!\n")
        runGame()

    except OSError:
        logging.warning("Cannot activate Windowed Mode!")
        print('''"\n{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(appName))
        time.sleep(2)
        main()


def fullScreenMode():
    """Full Screen Mode Launcher."""
    # Ask if they would like Ramp or MMX Emulation
    logging.info("Use Ramp Emulation or MMX Emulation?")
    print("""
Would you like to use Ramp Emulation or MMX Emulation?
Hint: Ramp Emulation works on almost all computers.

[r] Ramp Emulation
[m] MMX Emulation
[q] Quit""")

    graphicsModeInput = input("\n> ")

    if graphicsModeInput.lower() == "r":
        logging.info("User choose Ramp Emulation")
        graphicsMode = "Ramp Emulation"

    elif graphicsModeInput.lower() == "m":
        logging.info("User choose MMX Emulation")
        graphicsMode = "MMX Emulation"

    # Go back to the main menu
    else:
        main()

    logging.info("Creating Full Screen Mode registry strings")
    try:
        # Write registry strings
        strings.Write3DDeviceName(graphicsMode)
        strings.WriteFullScreen("YES")

        # TODO Should this be the value of the two strings?
        strings.WriteBuffers("YES")
        strings.WriteSurfaces("YES")

        logging.info("Full Screen Mode sucessfully activated")
        print("\nFull Screen Mode sucessfully activated!\n")
        runGame()

    except OSError:
        logging.warning("Cannot activate Full Screen Mode!")
        print("""\n{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.""".format(appName))
        time.sleep(2)
        main()


def selecttheIsland():
    """Manually select a LEGO Island installation if detection fails."""
    # Draw (then withdraw) the root Tk window
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the exe
    logging.info("Display file selection dialog for LEGO Island exe")
    manualGamePath = filedialog.askopenfilename(
        parent=root,
        title="Select your LEGO Island Executable (LEGOISLE.EXE)",
        defaultextension=".exe",
        filetypes=[("Windows Executable", "*.exe")]
    )

    # The user clicked the cancel button
    if not manualGamePath:
        # Give focus back to console window
        root.destroy()

        logging.warning("User did not select a LEGO Island installation!")
        print("\nCould not find a vaild LEGO Island installation!")
        main()

    # The user selected an installation
    else:
        try:
            # Display exit message
            logging.info("Display exit message")
            print("\nSee ya later, Brickulator!")

            logging.info("Run user-defined installation, located at {0}"
                         .format(manualGamePath))
            subprocess.call([manualGamePath])

            # Close app
            logging.info("{0} is shutting down".format(appName))
            raise SystemExit(0)

        # TODO I guess this works?
        except Exception:
            logging.warning("User-defined LEGO Island installation did not work!")
            print("\nCould not run {0} from {1}!".format(game, manualGamePath))

            logging.info("Re-running manual installation process")
            print("\nPlease select a new {0} installation".format(game))
            time.sleep(2)
            selecttheIsland()


if __name__ == "__main__":
    # Write window title (since there is no GUI)
    os.system("title {0} {1}{2}".format(appName, majVer, minVer))
    preload()
    main()
