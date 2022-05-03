from gendiff.engine import gen_files_diff


def read_file(file_path, mode='r'):
    with open(file_path, mode=mode, encoding='utf8') as f:
        return f.read()


def test_pretty_simple():
    expected = read_file('./tests/fixtures/pretty_simple.txt')
    result = gen_files_diff(
        './tests/fixtures/short_file1.json',
        './tests/fixtures/short_file2.json',
        format_='pretty'
    )
    assert expected == result


def test_pretty_complex():
    expected = read_file('./tests/fixtures/pretty_complex.txt')
    result = gen_files_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        format_='pretty'
    )
    assert expected == result
#
#
# def test2_json_complex():
#     assert json_complex == gen_files_diff()
#
#
# def test3_plain_simple():
#     assert plain_simple == gen_files_diff()
#
#
# def test4_plain_complex():
#     assert plain_complex == gen_files_diff()
#
#
# def test5_pretty_simple():
#     pass

