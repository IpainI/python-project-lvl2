import json

from gendiff.scripts import gen_diff


def render(file1, file2):
    return json.dumps(gen_diff(file1, file2))
