# Information Gathering Plugin
# Version 1.0

import platform
import os

def append(string):
    global data
    data += string + '\n'

append('USER: ' + platform.node())
append('PLATFORM: ' + platform.platform())
append('ARCHITECTURE: ' + platform.architecture()[0])
append('WINDOWS DIR: ' + os.environ['WINDIR'])

# End