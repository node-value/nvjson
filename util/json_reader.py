import os


def read_basic_cases() -> list:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_test_data/basic_cases")
    return [open(os.path.join(path, filename), 'r').read() for filename in os.listdir(path)]


def read_other_cases(file_name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_test_data/other_cases")
    return open(os.path.join(path, file_name), 'r').read()
