from gendiff import formatters
from gendiff.loader import get_file_content


def generate_diff(file1, file2, output_format='plain'):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)
    formatter = formatters.choose(output_format)
    return formatter.render(content1, content2)

