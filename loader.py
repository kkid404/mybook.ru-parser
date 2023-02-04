import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

USERNAME = config['MYBOOK']['LOGIN']
PASSWORD = config['MYBOOK']['PASSWORD']