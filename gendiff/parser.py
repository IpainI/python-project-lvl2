import json

import yaml


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    elif content in ('yaml', 'yml'):
        return yaml.safe_load(content)
    raise ValueError(f'Files with extension {extension} are not supported')
