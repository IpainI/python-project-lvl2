import json

from gendiff.scripts import gen_diff


def render(file1, file2):
    return json.dump(gen_diff(file1, file2))
