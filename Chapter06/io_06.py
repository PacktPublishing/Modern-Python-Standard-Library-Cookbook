import configparser


def read_config(config_text, schema=None):
    """Read options from ``config_text`` applying given ``schema``"""
    schema = schema or {}

    cfg = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    try:
        cfg.read_string(config_text)
    except configparser.MissingSectionHeaderError:
        config_text = '[main]\n' + config_text
        cfg.read_string(config_text)

    config = {}
    for section in schema:
        options = config.setdefault(section, {})
        for option, option_schema in schema[section].items():
            options[option] = option_schema.get('default')
    for section in cfg.sections():
        options = config.setdefault(section, {})
        section_schema = schema.get(section, {})
        for option in cfg.options(section):
            option_schema = section_schema.get(option, {})
            getter = 'get' + option_schema.get('type', '')
            options[option] = getattr(cfg, getter)(section, option)
    return config


config_text = '''
debug = true

[registry]
name = Alessandro
surname = Molina

[extra]
likes = spicy food
countrycode = 39
'''

config = read_config(config_text, {
    'main': {
        'debug': {'type': 'boolean'}
    },
    'registry': {
        'name': {'default': 'unknown'},
        'surname': {'default': 'unknown'},
        'middlename': {'default': ''},
    },
    'extra': {
        'countrycode': {'type': 'int'},
        'age': {'type': 'int', 'default': 0}
    },
    'more': {
        'verbose': {'type': 'int', 'default': 0}
    }
})

import pprint
pprint.pprint(config)