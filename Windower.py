"""
    This file is part of ICU (LEGO Island Configuration Utility)

    ICU - A collection of LEGO Island Configuration Tools
    Copyright 2012-2013 Triangle717 <http://triangle717.wordpress.com>

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

# ICU Windower V2.0.1
# Part of ICU (LEGO Island Configuration Utility)
# https://github.com/le717/ICU
# Copyright 2012-2013 Triangle717 (http://triangle717.wordpress.com).

import os, sys, time # General use modules
import winreg, platform # Main use module
import webbrowser, subprocess # Special purpose modules
import logging, yourscorecube # Logging Code
from tkinter import (filedialog, Tk) # File selection dialog

# Global variables
app = "ICU Windower"
majver = "Version 2.0.1"
minver = ""
creator = "Triangle717"
game = "LEGO Island"

# ------------ Begin ICU Windower Initialization ------------ #

def preload():
    '''Python 3.3.0 and Windows Architecture check'''

    logging.info("Begin logging to {0}".format(yourscorecube.logging_file))
    logging.info('''
                                #############################################
                                            {0} {1} {2}
                                        Copyright 2012-2013 {3}
                                                YourScoreCube.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/ICU/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))

     # You need to have at least Python 3.3.0 to run ICU Windower
    if sys.version_info < (3,3,0):
        logging.warning("You are not running Python 3.3.0 or higher!\nYou need to get a newer version to run {0}".format(app))
        sys.stdout.write("\nYou need to download Python 3.3.0 or greater to run {0} {1} {2}.".format(app, majver, minver))

        # Don't open browser immediately
        time.sleep(2)
        logging.info("Open new tab in web browser to http://python.org/download")
        webbrowser.open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)

        # Close ICU ReDirect
        logging.info("Display error message for three seconds")
        time.sleep(3)
        logging.info("{0} is shutting down.".format(app))
        raise SystemExit

    # If you are running Python 3.3.0
    else:
        logging.info("You are running Python 3.3.0 or greater. {0} will continue.".format(app))

        # Declare osbit global variable
        global osbit

        # User is running 64-bit Windows
        if platform.machine() == 'AMD64':
            logging.info("User is running 64-bit Windows.")
            osbit = "x64"
            logging.info("Swiching to main menu")
            main()

        # User is running 32-bit Windows
        elif platform.machine() == 'x86':
            logging.info("User is running 32-bit Windows.")
            osbit = "x86"
            logging.info("Swiching to main menu")
            main()

        # The user is running an unsupported version of Windows!
        else:
            logging.warning("User is running an unsupported OS!")
            print("\nYou are running an unsupported OS! {0} will now close.".format(app))
            time.sleep(3)
            logging.info("{0} is shutting down".format(app))
            raise SystemExit

# ------------ End ICU Windower Initialization ------------ #

# ------------ Begin ICU Windower Menu Layout ------------ #

def main():
    '''ICU Windower Menu Layout'''

    '''No, I did not forget something. This is all throughout the script
     to divide up the log a little bit when switching to new processes.'''
    logging.info('''

''')

    print("\nWelcome to {0} {1} {2}\nCopyright 2012-2013 {3}".format(app, majver, minver, creator))
    print('''\nPlease make a selection:\n
[f] Full Screen Mode
[w] Windowed Mode
[q] Quit''')
    logging.info("Display menu to user")
    menuopt = input("\n> ")
    while True:

        if menuopt.lower() == "f":
            logging.info("User pressed '[f] Full Screen Mode'")
            logging.info("Switching to Full Screen Mode introduction (FullScreen())")
            FullScreen()

        elif menuopt.lower() == "w":
            logging.info("User pressed '[w] Windowed Mode'")
            logging.info("Switching to Windowed Mode introduction (Windowed())")
            Windowed()


        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            print("\nGoodbye!")
            time.sleep(3)
            logging.info('''{0} is shutting down.
            '''.format(app))
            raise SystemExit

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()

# ------------ End ICU Windower Menu Layout ------------ #


# ------------ Begin Game Launching Code ------------ #

def letheIsland():
    '''Launches LEGO Island'''

    logging.info('''
''')

    if osbit == "x86":
        try:
            logging.info("Get LEGO Island Installation path from x86 Registry")
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape\LEGO Island') as gamefolder:
                gamepath = winreg.QueryValueEx(gamefolder, "diskpath")

            # Convert tuple to str(ing)
            logging.info("Convert tuple returned by Registry to a string")
            gamepath = str(gamepath)

            # Clean up string to get a clean folder path
            logging.info("Cleaning up installation folder path...")
            gamepath = gamepath.strip("(''), 1")
            logging.info("LEGO Island Installation located at {0}".format(gamepath))

        # ICU Windower could not properly find the game location, run with Admin rights, such and such.
        except WindowsError:
            logging.warning("{0} cannot detect LEGO Island installation!".format(game))
            print("{0} cannot detect a {1} installation!".format(app, game))
            time.sleep(3)

            # Ask if user wants to manually select the installation
            logging.info("Do you want to select an installation yourself?")
            print("Do you want to manually select a {0} installation?".format(game))
            manual_select = input("\n\n> ")

            # Nope, go back to the menu
            if manual_select.lower() != 'y':
                logging.warning("User does not want to manually select an installation!")
                time.sleep(1)
                logging.info("Switching to main menu")
                main()

            # Yes, I want to select an installation
            else:
                logging.info("User does want to manually select an installation")
                logging.info("Switching to selecttheIsland()")
                time.sleep(1)
                selecttheIsland()

    elif osbit == "x64":
        try:
            logging.info("Get LEGO Island Installation path from x64 Registry")
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape\LEGO Island') as gamefolder:
                gamepath = winreg.QueryValueEx(gamefolder, "diskpath")

            # Convert tuple to str(ing)
            logging.info("Convert tuple returned by Registry to a string")
            gamepath = str(gamepath)

            # Clean up string to get a clean folder path
            logging.info("Cleaning up folder path...")
            gamepath = gamepath.strip("(''), 1")
            logging.info("LEGO Island Installation located at {0}".format(gamepath))

        # ICU Windower could not properly find the game location, run with Admin rights, such and such.
        except WindowsError:
            logging.warning("{0} cannot detect LEGO Island installation!".format(game))
            print("{0} cannot detect a {1} installation!".format(app, game))
            time.sleep(3)

            # Ask if user wants to manually select the installation
            logging.info("Do you want to select an installation yourself?")
            print("Do you want to manually select a {0} installation?".format(game))
            manual_select = input("\n\n> ")

            # Nope, go back to the menu
            if manual_select.lower() != 'y':
                logging.warning("User does not want to manually select an installation!")
                time.sleep(1)
                logging.info("Switching to main menu")
                main()

            # Yes, I want to select an installation
            else:
                logging.info("User does want to manually select an installation")
                logging.info("Switching to selecttheIsland()")
                time.sleep(1)
                selecttheIsland()

    # Launch LEGO Island?
    logging.info("Do you want to play LEGO Island now?")
    print("\nDo you want to play {0} now? ".format(game) + r"(y\N)")
    rungame = input("\n> ")

    # No, don't launch it
    if rungame.lower() != "y":
        logging.warning("User does not want to play LEGO Island right now!")
        main()

    # Yes, launch it (User presses 'y', which is the only key that will run the game)
    else:
        time.sleep(1)
        try:

            # Display message
            logging.info("Display exit message")
            print("\nSee ya later, Brickulator!")

            # Run game
            logging.info('Run "legoisle.exe", located at {0}'.format(gamepath))
            # If the .exe name is all uppercase (as it installs) it will not load.
            # If it is all lowercase, it runs. Ah, the mysteries of the Island...
            subprocess.call([os.path.join(gamepath, "legoisle.exe")])

            # Close app
            logging.info("{0} is shutting down".format(app))
            raise SystemExit

        # Cannot find EXE at gamepath entered
        except OSError:
            logging.warning('Cannot find {0} installation at "{1}"!'.format(game, gamepath))
            print('\nCannot find {0} installation at\n"{1}"!'.format(game, gamepath))
            time.sleep(3)
            logging.info("Switching to main menu")
            main()

            # Ask if user wants to manually select the installation
            logging.info("Do you want to select an installation yourself?")
            print("Do you want to manually select a {0} installation?".format(game))
            manual_select = input("\n\n> ")

            # Nope, go back to the menu
            if manual_select.lower() != 'y':
                logging.warning("User does not want to manually select an installation!")
                time.sleep(1)
                logging.info("Switching to main menu")
                main()

            # Yes, I want to select an installation
            else:
                logging.info("User does want to manually select an installation")
                logging.info("Switching to selecttheIsland()")
                time.sleep(1)
                selecttheIsland()

# ------------ End Game Launching Code ------------ #


# ------------ Begin Windowed Intro ------------ #

def Windowed():
    '''Windowed Mode Launcher'''

    logging.info('''
''')

    # Switch to 32-bit registry string code
    if osbit == "x86":
        logging.info("User is running 32-bit (x86) Windows, use x86 Registry Strings")
        logging.info("Switch to eightsixWindowed()")
        eightsixWindowed()

    # Switch to 64-bit registry string code
    elif osbit == "x64":
        logging.info("User is running 64-bit (x64) Windows, use x64 Registry Strings")
        logging.info("Switch to sixfourWindowed()")
        sixfourWindowed()

# ------------ End Windowed Intro ------------ #


# ------------ Begin Windowed code for Windows x86 ------------ #

def eightsixWindowed():
    '''Activates LEGO Island Windowed Mode on Windows x86'''

    logging.info('''
''')

    logging.info("Creating Windowed Mode registry strings (x86)")
    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")
            winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "Ramp Emulation")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ, "NO")

        logging.info("Windowed Mode sucessfully activated")
        print("\nWindowed Mode sucessfully activated!\n")
        logging.info("Switching to game launching process (letheIsland())")
        letheIsland()

    except WindowsError:
        logging.warning("Cannot activate Windowed Mode!")
        logging.warning("{0} was not run with Administrator rights, which are needed to activate Windowed Mode!".format(app))
        print("\n{0} does not have the user rights to operate!\nPlease relaunch {1} as an Administrator.".format(app, app))
        time.sleep(3)
        logging.info("Switching to main menu")
        main()

# ------------ End Windowed code for Windows x86 ------------ #


# ------------ Begin Windowed code for Windows x64 ------------ #

def sixfourWindowed():
    '''Activates LEGO Island Windowed Mode on Windows x64'''

    logging.info('''
''')

    logging.info("Creating Windowed Mode registry strings (x64)")
    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")
            winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "Ramp Emulation")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ, "NO")

        logging.info("Windowed Mode sucessfully activated")
        print("\nWindowed Mode sucessfully activated!\n")
        logging.info("Switching to game launching process (letheIsland())")
        letheIsland()

    except WindowsError:
        logging.warning("Cannot activate Windowed Mode!")
        logging.warning("{0} was not run with Administrator rights, which are needed to activate Windowed Mode!".format(app))
        print("\n{0} does not have the user rights to operate!\nPlease relaunch {1} as an Administrator.".format(app, app))
        time.sleep(3)
        logging.info("Switching to main menu")
        main()

# ------------ End Windowed code for Windows x64 ------------ #


# ------------ Begin Full Screen Intro ------------ #

def FullScreen():
    '''Full Screen Mode Launcher'''

    logging.info('''
''')


    # Ask if they would like Ramp or MMX Emulation
    logging.info("Do you want to use Ramp or MMX Emulation?")
    logging.info("When in doubt, use Ramp.")
    print('''\nWould you like to use Ramp or MMX Emulation?
Hint: Ramp Emulation works on almost all computers.
\n[r] Ramp Emulation
[m] MMX Emulation''')

    graphicsmode = input("\n> ")

    if graphicsmode.lower() == "r":
        logging.info("User choose Ramp Emulation")
        graphicsmode = "Ramp"

    elif graphicsmode.lower() == "m":
        logging.info("User choose MMX Emulation")
        graphicsmode = "MMX"

    # Switch to 32-bit registry string code
    if osbit == "x86":
        logging.info("User is running 32-bit (x86) Windows, use x86 Registry Strings")
        logging.info("Switch to eightsixFullScreen(graphicsmode)")
        eightsixFullScreen(graphicsmode)

    # Switch to 64-bit registry string code
    elif osbit == "x64":
        logging.info("User is running 64-bit (x64) Windows, use x64 Registry Strings")
        logging.info("Switch to sixfourFullScreen(graphicsmode)")
        sixfourFullScreen(graphicsmode)

# ------------ End Full Screen Intro ------------ #


# ------------ Begin Windowed code for Windows x86 ------------ #

def eightsixFullScreen(graphicsmode):
    '''Restores LEGO Island Full Screen Mode on Windows x86'''

    logging.info('''
''')

    logging.info("Creating Full Screen Mode registry strings (x86)")

    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ, "YES")

            # Recall that user selected Ramp Emulation
            if graphicsmode == "Ramp":
                winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "Ramp Emulation")

            # Recall that user selected MMX Emulation
            else: # elif graphicsmode == "MMX":
                winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "MMX Emulation")

        logging.info("Full Screen Mode sucessfully activated")
        print("\nFull Screen Mode sucessfully activated!\n")
        logging.info("Switching to game launching process (letheIsland())")
        letheIsland()

    except WindowsError:
        logging.warning("Cannot activate Full Screen Mode!")
        logging.warning("{0} was not run with Administrator rights, which are needed to activate Full Screen Mode!".format(app))
        print("\n{0} does not have the user rights to operate!\nPlease relaunch {1} as an Administrator.".format(app, app))
        time.sleep(3)
        logging.info("Switching to main menu")
        main()

# ------------ End Windowed code for Windows x86 ------------ #


# ------------ Begin Windowed code for Windows x64 ------------ #

def sixfourFullScreen(graphicsmode):
    '''Restores LEGO Island Full Screen Mode on Windows x64'''

    logging.info('''
''')

    logging.info("Creating Full Screen Mode registry strings (x64)")

    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ, "YES")

            # Recall that user selected Ramp Emulation
            if graphicsmode == "Ramp":
                winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "Ramp Emulation")

            # Recall that user selected MMX Emulation
            else: # elif graphicsmode == "MMX":
                winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "MMX Emulation")

        logging.info("Full Screen Mode sucessfully activated")
        print("\nFull Screen Mode sucessfully activated!\n")
        logging.info("Switching to game launching process (letheIsland()")
        letheIsland()

    except WindowsError:
        logging.warning("Cannot activate Full Screen Mode!")
        logging.warning("{0} was not run with Administrator rights, which are needed to activate Full Screen Mode!".format(app))
        print("\n{0} does not have the user rights to operate!\nPlease relaunch {1} as an Administrator.".format(app, app))
        time.sleep(3)
        logging.info("Switching to main menu")
        main()

# ------------ End Windowed code for Windows x64 ------------ #


# ------------ Began Manual LEGO Island Installation Selection ------------ #

def selecttheIsland():
    '''Manually Select a LEGO Island Installation if Detection Fails'''

    # File format label
    fileformat = [("Windows Executable", "*.exe")]

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to practically hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the patch file
    # TODO: How can I say to select LEGOISLE.EXE for an EXE with a different name?
    logging.info("Display file selection dialog for LEGO Island EXE")
    manualgamepath = filedialog.askopenfilename(
    parent=root,
    title="Select your LEGO Island Executable (LEGOISLE.EXE)",
    defaultextension=".exe",
    filetypes=fileformat)

    # The user clicked the cancel button
    if len(manualgamepath) == 0:

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select their LEGO Island installation!")
        print("\nCould not find a vaild LEGO Island installation!")
        time.sleep(1)

        logging.info("Proceeding to main menu")
        main()

    # The user selected an installation
    else:
        try:

            # Display exit message
            logging.info("Display exit message")
            print("\nSee ya later, Brickulator!")

            logging.info('Run user-defined installation, located at {0}'.format(manualgamepath))
            subprocess.call([manualgamepath])

            # Close app
            logging.info("{0} is shutting down".format(app))
            raise SystemExit

        # I guess this works?
        except Exception:
            logging.warning("User-defined LEGO Island installation did not work!")
            print("\nCould not run {0} from {1}!".format(game, manualgamepath))

            logging.info("Re-running manual installation process (selecttheIsland())")
            print("\nPlease select a new {0} installation".format(game))
            time.sleep(2)
            selecttheIsland()

# ------------ End Manual LEGO Island Installation Selection ------------ #

if __name__ == "__main__":
    # Write window title (since there is no GUI)
    os.system("title {0} {1} {2}".format(app, majver, minver))
    # Run preload() to begin ICU Windower Initialization
    preload()