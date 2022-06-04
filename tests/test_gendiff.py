#!/usr/bin/env python3
from gendiff import generate_diff


def read_file(file_path, mode='r'):
    with open(file_path, mode=mode, encoding='utf8') as f:
        return f.read()


def test_pretty_simple():
    expected = read_file('./tests/fixtures/pretty_simple.txt')
    result = generate_diff(
        './tests/fixtures/short_file1.json',
        './tests/fixtures/short_file2.json',
        output_format='pretty'
    )
    with open('./tests/fixtures/result1.txt', 'w') as a:
        a.write(result)
    assert expected == result


def test_pretty_complex():
    expected = read_file('./tests/fixtures/pretty_complex.txt')
    result = generate_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        output_format='pretty'
    )
    with open('./tests/fixtures/result2.txt', 'w') as a:
        a.write(result)
    assert expected == result


def test_plain_complex():
    expected = read_file('./tests/fixtures/plain_complex.txt')
    result = generate_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        output_format='plain'
    )
    with open('./tests/fixtures/result3.txt', 'w') as a:
        a.write(result)
    assert expected == result



