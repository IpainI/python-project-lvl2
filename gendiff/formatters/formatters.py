from gendiff.formatters import plain, pretty, json


def choose(out_format):
    formatters = {
        'plain': plain,
        'stylish': pretty,
        'json': json,
    }
    if not out_format:
        return stylish
    return formatters[out_format]
    
