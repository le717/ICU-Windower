# -*- coding: utf-8 -*-
"""
    This file is part of ICU (LEGO Island Configuration Utility)

    ICU - A collection of LEGO Island Configuration Tools
    Created 2012-2013 Triangle717 <http://Triangle717.WordPress.com>

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
# ICU (LEGO Island Configuration Utility)
# https://github.com/le717/ICU

import winreg
import platform

x86regpath = "Software\Mindscape\LEGO Island"
x64regpath = "Software\Wow6432Node\Mindscape\LEGO Island"

# Get the Windows architecture
if platform.machine() == "AMD64":
    # x64 Windows == True
    osbit = True
else:
    # x86 Windows == False
    osbit = False

# ------------ Begin 3D Device Name Strings ------------ #


def Write3DDeviceName(value):
    """Write '3D Device Name' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _Write3DDeviceName64(value)
    elif not osbit:
        # If x86 Windows, use x86 strings
        _Write3DDeviceName86(value)


def Read3DDeviceName():
    """Read '3D Device Name' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _Read3DDeviceName64()
    else:
        # If x86 Windows, use x86 strings
        return _Read3DDeviceName86()


def _Write3DDeviceName86(value):
    """Write x86 '3D Device Name' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as devicename:
        winreg.SetValueEx(devicename, "3D Device Name",
                          0, winreg.REG_SZ, value)


def _Read3DDeviceName86():
    """Read x86 '3D Device Name' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as devicestring:
        devicename = winreg.QueryValueEx(devicestring, "3D Device Name")

    # Get only the value of the returned tuple
    devicename = devicename[0]
    return devicename


def _Write3DDeviceName64(value):
    """Write x64 '3D Device Name' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as devicename:
        winreg.SetValueEx(devicename, "3D Device Name",
                          0, winreg.REG_SZ, value)


def _Read3DDeviceName64():
    """Read x64 '3D Device Name' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as devicestring:
        devicename = winreg.QueryValueEx(devicestring, "3D Device Name")

    # Get only the value of the returned tuple
    devicename = devicename[0]
    return devicename

# ------------ End 3D Device Name Strings ------------ #


# ------------ Begin 3DSound Strings ------------ #

def Write3DSound(value):
    """Write '3DSound' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _Write3DSound64(value)
    else:
        # If x86 Windows, use x86 strings
        _Write3DSound86(value)


def Read3DSound():
    """Read '3DSound' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _Read3DSound64()
    else:
        # If x86 Windows, use x86 strings
        return _Read3DSound86()


def _Write3DSound86(value):
    """Write x86 '3DSound' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as soundsetting:
        winreg.SetValueEx(soundsetting, "3DSound", 0, winreg.REG_SZ, value)


def _Read3DSound86():
    """Read x86 '3DSound' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as soundstring:
        soundsetting = winreg.QueryValueEx(soundstring, "3DSound")

    # Get only the value of the returned tuple
    soundsetting = soundsetting[0]
    return soundsetting


def _Write3DSound64(value):
    """Write x64 '3DSound' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as soundsetting:
        winreg.SetValueEx(soundsetting, "3DSound", 0, winreg.REG_SZ, value)


def _Read3DSound64():
    """Read x64 '3DSound' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as soundstring:
        soundsetting = winreg.QueryValueEx(soundstring, "3DSound")

    # Get only the value of the returned tuple
    soundsetting = soundsetting[0]
    return soundsetting

# ------------ End 3DSound Strings ------------ #


# ------------ Begin Back Buffers in Video RAM Strings ------------ #

def WriteBuffers(value):
    """Write 'Back Buffers in Video RAM' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteBuffers64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteBuffers86(value)


def ReadBuffers():
    """Read 'Back Buffers in Video RAM' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadBuffers64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadBuffers86()


def _WriteBuffers86(value):
    """Write x86 'Back Buffers in Video RAM' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as buffersetting:
        winreg.SetValueEx(buffersetting, "Back Buffers in Video RAM",
                          0, winreg.REG_SZ, value)


def _ReadBuffers86():
    """Read x86 'Back Buffers in Video RAM' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as bufferstring:
        buffersetting = winreg.QueryValueEx(
            bufferstring, "Back Buffers in Video RAM")

    # Get only the value of the returned tuple
    buffersetting = buffersetting[0]
    return buffersetting


def _WriteBuffers64(value):
    """Write x64 'Back Buffers in Video RAM' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as buffersetting:
        winreg.SetValueEx(buffersetting, "Back Buffers in Video RAM",
                          0, winreg.REG_SZ, value)


def _ReadBuffers64():
    """Read x64 'Back Buffers in Video RAM' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as bufferstring:
        buffersetting = winreg.QueryValueEx(
            bufferstring, "Back Buffers in Video RAM")

    # Get only the value of the returned tuple
    buffersetting = buffersetting[0]
    return buffersetting

# ------------ End Back Buffers in Video RAM Strings ------------ #


# ------------ Begin diskpath Strings ------------ #

def WriteDiskPath(value):
    """Write 'diskpath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteDiskPath64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteDiskPath86(value)


def ReadDiskPath():
    """Read 'diskpath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadDiskPath64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadDiskPath86()


def _WriteDiskPath86(value):
    """Write x86 'diskpath' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as diskpath:
        winreg.SetValueEx(diskpath, "diskpath", 0, winreg.REG_SZ, value)


def _ReadDiskPath86():
    """Read x86 'diskpath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as diskstring:
        diskpath = winreg.QueryValueEx(diskstring, "diskpath")

    # Get only the value of the returned tuple
    diskpath = diskpath[0]
    return diskpath


def _WriteDiskPath64(value):
    """Write x64 'diskpath' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as diskpath:
        winreg.SetValueEx(diskpath, "diskpath", 0, winreg.REG_SZ, value)


def _ReadDiskPath64():
    """Read x64 'diskpath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as diskstring:
        diskpath = winreg.QueryValueEx(diskstring, "diskpath")

    # Get only the value of the returned tuple
    diskpath = diskpath[0]
    return diskpath

# ------------ End diskpath Strings ------------ #


# ------------ Begin Display Bit Depth Strings ------------ #

def WriteDisplayBit(value):
    """Write 'Display Bit Depth' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteDisplayBit64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteDisplayBit86(value)


def ReadDisplayBit():
    """Read 'Display Bit Depth' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadDisplayBit64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadDisplayBit86()


def _WriteDisplayBit86(value):
    """Write x86 'Display Bit Depth' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as colorbit:
        winreg.SetValueEx(colorbit, "Display Bit Depth",
                          0, winreg.REG_SZ, value)


def _ReadDisplayBit86():
    """Read x86 'Display Bit Depth' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as stringcolor:
        colorbit = winreg.QueryValueEx(stringcolor, "Display Bit Depth")

    # Get only the value of the returned tuple
    colordepth = colorbit[0]
    return colordepth


def _WriteDisplayBit64(value):
    """Write x64 'Display Bit Depth' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as colorbit:
        winreg.SetValueEx(colorbit, "Display Bit Depth",
                          0, winreg.REG_SZ, value)


def _ReadDisplayBit64():
    """Read x64 'Display Bit Depth' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as stringcolor:
        colorbit = winreg.QueryValueEx(stringcolor, "Display Bit Depth")

    # Get only the value of the returned tuple
    colordepth = colorbit[0]
    return colordepth

# ------------ End Display Bit Depth Strings ------------ #


# ------------ Begin Draw Cursor Strings ------------ #

def WriteDrawCursor(value):
    """Write 'Draw Cursor' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteDrawCursor64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteDrawCursor86(value)


def ReadDrawCursor():
    """Read 'Draw Cursor' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadDrawCursor64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadDrawCursor86()


def _WriteDrawCursor86(value):
    """Write x86 'Draw Cursor' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as cursor:
        winreg.SetValueEx(cursor, "Draw Cursor", 0, winreg.REG_SZ, value)


def _ReadDrawCursor86():
    """Read x86 'Draw Cursor' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as cursorstring:
        cursor = winreg.QueryValueEx(cursorstring, "Draw Cursor")

    # Get only the value of the returned tuple
    cursor = cursor[0]
    return cursor


def _WriteDrawCursor64(value):
    """Write x64 'Draw Cursor' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as cursor:
        winreg.SetValueEx(cursor, "Draw Cursor", 0, winreg.REG_SZ, value)


def _ReadDrawCursor64():
    """Read x64 'Draw Cursor' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as cursorstring:
        cursor = winreg.QueryValueEx(cursorstring, "Draw Cursor")

    # Get only the value of the returned tuple
    cursor = cursor[0]
    return cursor

# ------------ End Draw Cursor Strings ------------ #


# ------------ Begin Flip Surfaces Strings ------------ #

def WriteSurfaces(value):
    """Write 'Flip Surfaces' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteSurfaces64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteSurfaces86(value)


def ReadSurfaces():
    """Read 'Flip Surfaces' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadSurfaces64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadSurfaces86()


def _WriteSurfaces86(value):
    """Write x86 'Flip Surfaces' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as surfaces:
        winreg.SetValueEx(surfaces, "Flip Surfaces", 0, winreg.REG_SZ, value)


def _ReadSurfaces86():
    """Read x86 'Flip Surfaces' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as surfacesstring:
        surfaces = winreg.QueryValueEx(surfacesstring, "Flip Surfaces")

    # Get only the value of the returned tuple
    surfaces = surfaces[0]
    return surfaces


def _WriteSurfaces64(value):
    """Write x64 'Flip Surfaces' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as surfaces:
        winreg.SetValueEx(surfaces, "Flip Surfaces", 0, winreg.REG_SZ, value)


def _ReadSurfaces64():
    """Read x64 'Flip Surfaces' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as surfacesstring:
        surfaces = winreg.QueryValueEx(surfacesstring, "Flip Surfaces")

    # Get only the value of the returned tuple
    surfaces = surfaces[0]
    return surfaces

# ------------ End Flip Surfaces Strings ------------ #


# ------------ Begin Full Screen Strings ------------ #

def WriteFullScreen(value):
    """Write 'Full Screen' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteFullScreen64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteFullScreen86(value)


def ReadFullScreen():
    """Read 'Full Screen' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadFullScreen64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadFullScreen86()


def _WriteFullScreen86(value):
    """Write x86 'Full Screen' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as fullscreen:
        winreg.SetValueEx(fullscreen, "Full Screen", 0, winreg.REG_SZ, value)


def _ReadFullScreen86():
    """Read x86 'Full Screen' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as fullscreenstring:
        fullscreen = winreg.QueryValueEx(fullscreenstring, "Full Screen")

    # Get only the value of the returned tuple
    fullscreen = fullscreen[0]
    return fullscreen


def _WriteFullScreen64(value):
    """Write x64 'Full Screen' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as fullscreen:
        winreg.SetValueEx(fullscreen, "Full Screen", 0, winreg.REG_SZ, value)


def _ReadFullScreen64():
    """Read x64 'Full Screen' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as fullscreenstring:
        fullscreen = winreg.QueryValueEx(fullscreenstring, "Full Screen")

    # Get only the value of the returned tuple
    fullscreen = fullscreen[0]
    return fullscreen

# ------------ End Full Screen Strings ------------ #


# ------------ Begin Island Quality Strings ------------ #


def WriteIslandQuality(value):
    """Write 'Island Quality' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteIslandQuality64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteIslandQuality86(value)


def ReadIslandQuality():
    """Read 'Island Quality' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadIslandQuality64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadIslandQuality86()


def _WriteIslandQuality86(value):
    """Write x86 'Island Quality' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as quality:
        winreg.SetValueEx(quality, "Island Quality", 0, winreg.REG_SZ, value)


def _ReadIslandQuality86():
    """Read x86 'Island Quality' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as qualitystring:
        quality = winreg.QueryValueEx(qualitystring, "Island Quality")

    # Get only the value of the returned tuple
    quality = quality[0]
    return quality


def _WriteIslandQuality64(value):
    """Write x64 'Island Quality' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as quality:
        winreg.SetValueEx(quality, "Island Quality", 0, winreg.REG_SZ, value)


def _ReadIslandQuality64():
    """Read x64 'Island Quality' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as qualitystring:
        quality = winreg.QueryValueEx(qualitystring, "Island Quality")

    # Get only the value of the returned tuple
    quality = quality[0]
    return quality


# ------------ End Island Quality Strings ------------ #


# ------------ Begin Island Texture Strings ------------ #

def WriteIslandTexture(value):
    """Write 'Island Texture' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteIslandTexture64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteIslandTexture86(value)


def ReadIslandTexture():
    """Read 'Island Texture' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadIslandTexture64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadIslandTexture86()


def _WriteIslandTexture86(value):
    """Write x86 'Island Texture' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as texture:
        winreg.SetValueEx(texture, "Island Texture", 0, winreg.REG_SZ, value)


def _ReadIslandTexture86():
    """Read x86 'Island Texture' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as texturestring:
        texture = winreg.QueryValueEx(texturestring, "Island Texture")

    # Get only the value of the returned tuple
    texture = texture[0]
    return texture


def _WriteIslandTexture64(value):
    """Write x64 'Island Texture' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as texture:
        winreg.SetValueEx(texture, "Island Texture", 0, winreg.REG_SZ, value)


def _ReadIslandTexture64():
    """Read x64 'Island Texture' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as texturestring:
        texture = winreg.QueryValueEx(texturestring, "Island Texture")

    # Get only the value of the returned tuple
    texture = texture[0]
    return texture


# ------------ End Island Texture Strings ------------ #


# ------------ Begin JoystickIndex Strings ------------ #

def WriteJoystickIndex(value):
    """Write 'JoystickIndex"' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteJoystickIndex64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteJoystickIndex86(value)


def ReadJoystickIndex():
    """Read 'JoystickIndex' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadJoystickIndex64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadJoystickIndex86()


def _WriteJoystickIndex86(value):
    """Write x86 'JoystickIndex' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as joystick:
        winreg.SetValueEx(joystick, "JoystickIndex", 0, winreg.REG_SZ, value)


def _ReadJoystickIndex86():
    """Read x86 'JoystickIndex' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as joystickstring:
        joystick = winreg.QueryValueEx(joystickstring, "JoystickIndex")

    # Get only the value of the returned tuple
    joystick = joystick[0]
    return joystick


def _WriteJoystickIndex64(value):
    """Write x64 'JoystickIndex' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as joystick:
        winreg.SetValueEx(joystick, "JoystickIndex", 0, winreg.REG_SZ, value)


def _ReadJoystickIndex64():
    """Read x64 'JoystickIndex' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as joystickstring:
        joystick = winreg.QueryValueEx(joystickstring, "JoystickIndex")

    # Get only the value of the returned tuple
    joystick = joystick[0]
    return joystick

# ------------ End JoystickIndex Strings ------------ #


# ------------ Begin moviespath Strings ------------ #

def WriteMoviesPath(value):
    """Write 'moviespath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteMoviesPath64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteMoviesPath86(value)


def ReadMoviesPath():
    """Read 'moviespath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadMoviesPath64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadMoviesPath86()


def _WriteMoviesPath86(value):
    """Write x86 'moviespath' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as moviespath:
        winreg.SetValueEx(moviespath, "moviespath", 0, winreg.REG_SZ, value)


def _ReadMoviesPath86():
    """Read x86 'moviespath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as moviesstring:
        moviespath = winreg.QueryValueEx(moviesstring, "moviespath")

    # Get only the value of the returned tuple
    moviespath = moviespath[0]
    return moviespath


def _WriteMoviesPath64(value):
    """Write x64 'moviespath' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as moviespath:
        winreg.SetValueEx(moviespath, "moviespath", 0, winreg.REG_SZ, value)


def _ReadMoviesPath64():
    """Read x64 'moviespath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as moviesstring:
        moviespath = winreg.QueryValueEx(moviesstring, "moviespath")

    # Get only the value of the returned tuple
    moviespath = moviespath[0]
    return moviespath


# ------------ End moviespath Strings ------------ #


# ------------ Begin Music Strings ------------ #

def WriteMusic(value):
    """Write 'Music' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteMusic64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteMusic86(value)


def ReadMusic():
    """Read 'Music' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadMusic64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadMusic86()


def _WriteMusic86(value):
    """Write x86 'Music' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as music:
        winreg.SetValueEx(music, "Music", 0, winreg.REG_SZ, value)


def _ReadMusic86():
    """Read x86 'Music' String"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as musicstring:
        music = winreg.QueryValueEx(musicstring, "Music")

    # Get only the value of the returned tuple
    music = music[0]
    return music


def _WriteMusic64(value):
    """Write x64 'Music' String"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as music:
        winreg.SetValueEx(music, "Music", 0, winreg.REG_SZ, value)


def _ReadMusic64():
    """Read x64 'Music' String"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as musicstring:
        music = winreg.QueryValueEx(musicstring, "Music")

    # Get only the value of the returned tuple
    music = music[0]
    return music


# ------------ End Music Strings ------------ #


# ------------ Begin savepath Strings ------------ #

def WriteSavePath(value):
    """Write 'savepath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteSavePath64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteSavePath86(value)


def ReadSavePath():
    """Read 'savepath' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadSavePath64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadSavePath86()


def _WriteSavePath86(value):
    """Write x86 'savepath' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x86regpath) as savepath:
        winreg.SetValueEx(savepath, "savepath", 0, winreg.REG_SZ, value)


def _ReadSavePath86():
    """Read x86 'savepath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x86regpath) as savestring:
        savepath = winreg.QueryValueEx(savestring, "savepath")

    # Get only the value of the returned tuple
    savepath = savepath[0]
    return savepath


def _WriteSavePath64(value):
    """Write x64 'savepath' string"""
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, x64regpath) as savepath:
        winreg.SetValueEx(savepath, "savepath", 0, winreg.REG_SZ, value)


def _ReadSavePath64():
    """Read x64 'savepath' string"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, x64regpath) as savestring:
        savepath = winreg.QueryValueEx(savestring, "savepath")

    # Get only the value of the returned tuple
    savepath = savepath[0]
    return savepath


# ------------ End savepath Strings ------------ #


# ------------ Begin UseJoystick Strings ------------ #


def WriteUseJoystick(value):
    """Write 'UseJoystick' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteUseJoystick64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteUseJoystick86(value)


def ReadUseJoystick():
    """Read 'UseJoystick' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadUseJoystick64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadUseJoystick86()


def _WriteUseJoystick86(value):
    """Write x86 'UseJoystick' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as usejoystick:
        winreg.SetValueEx(usejoystick, "UseJoystick", 0, winreg.REG_SZ, value)


def _ReadUseJoystick86():
    """Read x86 'UseJoystick' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as joystickinuse:
        usejoystick = winreg.QueryValueEx(joystickinuse, "UseJoystick")

    # Get only the value of the returned tuple
    usejoystick = usejoystick[0]
    return usejoystick


def _WriteUseJoystick64(value):
    """Write x64 'UseJoystick' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as fullscreen:
        winreg.SetValueEx(fullscreen, "UseJoystick", 0, winreg.REG_SZ, value)


def _ReadUseJoystick64():
    """Read x86 'UseJoystick' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as joystickinuse:
        usejoystick = winreg.QueryValueEx(joystickinuse, "UseJoystick")

    # Get only the value of the returned tuple
    usejoystick = usejoystick[0]
    return usejoystick


# ------------ End UseJoystick Strings ------------ #


# ------------ Begin Wide View Angle Strings ------------ #

def WriteWideAngle(value):
    """Write 'Wide View Angle' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        _WriteWideAngle64(value)
    else:
        # If x86 Windows, use x86 strings
        _WriteWideAngle86(value)


def ReadWideAngle():
    """Read 'Wide View Angle' string"""
    if osbit:
        # If x64 Windows, use x64 strings
        return _ReadWideAngle64()
    else:
        # If x86 Windows, use x86 strings
        return _ReadWideAngle86()


def _WriteWideAngle86(value):
    """Write x86 'Wide View Angle' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as wideviewangle:
        winreg.SetValueEx(wideviewangle, "Wide View Angle",
                          0, winreg.REG_SZ, value)


def _ReadWideAngle86():
    """Read x86 'Wide View Angle' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x86regpath) as wideanglestring:
        wideviewangle = winreg.QueryValueEx(wideanglestring, "Wide View Angle")

    # Get only the value of the returned tuple
    wideviewangle = wideviewangle[0]
    return wideviewangle


def _WriteWideAngle64(value):
    """Write x64 'Wide View Angle' string"""
    with winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as wideviewangle:
        winreg.SetValueEx(wideviewangle, "Wide View Angle",
                          0, winreg.REG_SZ, value)


def _ReadWideAngle64():
    """Read x64 'Wide View Angle' string"""
    with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, x64regpath) as wideanglestring:
        wideviewangle = winreg.QueryValueEx(wideanglestring, "Wide View Angle")

    # Get only the value of the returned tuple
    wideviewangle = wideviewangle[0]
    return wideviewangle

# ------------ End Wide View Angle Strings ------------ #
