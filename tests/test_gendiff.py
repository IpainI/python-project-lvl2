#!/usr/bin/env python3
import json
import yaml
from gendiff.engine import gen_diff
from gendiff.cli import text_format
from tests.fixtures.results import *


def test1_json_simple():
    print('./tests/fixtures/short_file1.json', './tests/fixtures/short_file2.json')
    assert json_simple == gen_diff(
        json.load(open('./tests/fixtures/short_file1.json')),
        json.load(open('./tests/fixtures/short_file2.json'))
    )


def test2_json_complex():
    assert json_complex == gen_diff()


def test3_plain_simple():
    assert plain_simple == gen_diff()


def test4_plain_complex():
    assert plain_complex == gen_diff()


def test5_pretty_simple():
    pass

