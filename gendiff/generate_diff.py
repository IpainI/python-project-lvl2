from gendiff import formatters
from gendiff.loader import get_file_content


def generate_diff(file1, file2, stylish='pretty'):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)
    formatter = formatters.choose(stylish)
    return formatter.render(content1, content2)
