import platform

def append(string):
	global data
	data += string + '\n'

append('USER: ' + platform.node())
append('PLATFORM: ' + platform.platform())