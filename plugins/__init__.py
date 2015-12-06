# Plugin Initialize


import ConfigParser
import os

__plugins__ = {}

plugins_dir = os.path.join(os.path.abspath(os.getcwdu()), 'plugins')
# initialize plugins directory
for _file in os.listdir(plugins_dir):
    plugins_path = os.path.join(plugins_dir, _file)
    if os.path.isdir(plugins_path):
        config_path = os.path.join(plugins_path, 'config.cfg')
        icon_path = os.path.join(plugins_path, 'icon.png')
        if os.path.exists(config_path) and os.path.exists(icon_path):
            Config = ConfigParser.ConfigParser()
            Config.read(config_path)
            try:
                __plugins__[_file] = {}
                __plugins__[_file]['name'] = Config.get('main', 'name')
                __plugins__[_file]['version'] = Config.get('main', 'version')
                __plugins__[_file]['author'] = Config.get('main', 'author')
                __plugins__[_file]['icon'] = icon_path
            except ConfigParser.NoOptionError, ConfigParser.NoSectionError:
                pass