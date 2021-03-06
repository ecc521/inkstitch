# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

import sys
from os.path import expanduser, realpath


def guess_inkscape_config_path():
    if getattr(sys, 'frozen', None):
        path = realpath(sys._MEIPASS.split('extensions', 1)[0])
        if sys.platform == "win32":
            import win32api

            # This expands ugly things like EXTENS~1
            path = win32api.GetLongPathName(path)
    else:
        path = expanduser("~/.config/inkscape")

    return path
