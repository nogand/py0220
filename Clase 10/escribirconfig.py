import configparser

config = configparser.ConfigParser()

config['settings']={'resolution':'320x240',
'color':'blue'}

config['date']={'year':'2020',
'month':'May',
'day': 27}

with open('example.ini', 'w') as configfile:
    config.write(configfile)
