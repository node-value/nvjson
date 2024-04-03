import json
import unittest

import nvjson
from util import json_reader


def read_file(file_name):
    return json.loads(json_reader.read_other_cases(file_name))


class MyTestCase(unittest.TestCase):
    def test_dict_encoding(self):
        to_compress_dict: dict = read_file("json_to_compress_dict.json")

        byte_str = nvjson.dumps(to_compress_dict)
        d = nvjson.loads(byte_str)
        self.assertEqual(d, to_compress_dict)

    def test_list_encoding(self):
        to_compress_list: dict = read_file("json_to_compress_list.json")

        byte_str = nvjson.dumps(to_compress_list)
        d = nvjson.loads(byte_str)
        self.assertEqual(d, to_compress_list)

    def test_dict_list_decoding(self):
        to_compress_dict_list: dict = read_file("json_to_compress_dict_list.json")

        byte_str = nvjson.dumps(to_compress_dict_list)
        d = nvjson.loads(byte_str)
        self.assertEqual(d, to_compress_dict_list)

    def test_huge_case(self):
        huge_case = read_file("citm_catalog.json")

        byte_str = nvjson.dumps(huge_case)
        d = nvjson.loads(byte_str)
        self.assertEqual(d, huge_case)


if __name__ == '__main__':
    unittest.main()
