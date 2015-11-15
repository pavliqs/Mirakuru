import platform

def append(string):
	global printf
	printf += string + '\n'

append('USER: ' + platform.node())
append('PLATFORM: ' + platform.platform())