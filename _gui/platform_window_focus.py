import ctypes
import ctypes.util
import sys

_is_osx = sys.platform == "darwin"

if _is_osx:
    appkit = ctypes.cdll.LoadLibrary(ctypes.util.find_library('AppKit'))
    objc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('objc'))

    objc.objc_getClass.restype = ctypes.c_void_p
    objc.sel_registerName.restype = ctypes.c_void_p
    objc.objc_msgSend.restype = ctypes.c_void_p
    objc.objc_msgSend.argtypes = [ctypes.c_void_p, ctypes.c_void_p]


def platform_window_focus(frame):
    """
    Focus the window frame
    """

    # General window raising
    if frame.IsIconized():
        frame.Iconize(False)
    if not frame.IsShown():
        frame.Show(True)
    frame.Raise()

    # OSX specific extra to ensure raise
    if _is_osx:
        try:
            NSApplication = ctypes.c_void_p(objc.objc_getClass('NSApplication'))
            NSApp = ctypes.c_void_p(objc.objc_msgSend(NSApplication, objc.sel_registerName('sharedApplication')))
            objc.objc_msgSend(NSApp, objc.sel_registerName('activateIgnoringOtherApps:'), True)
        except:
            # Failed to bring window to top in OSX
            pass
