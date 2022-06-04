from gendiff.parser import parse


def get_file_content(file_path):
    extension = file_path.split('.')[-1]
    with open(file_path, mode='r', encoding='utf8') as f:
        return parse(f.read(), extension)
