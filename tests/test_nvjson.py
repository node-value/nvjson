import unittest
from common.constants import Boundaries
import nvjson
import json
from util import json_reader


class TestNVJson(unittest.TestCase):
    basic_cases: list = list(map(lambda x: json.loads(x), json_reader.read_basic_cases()))

    def test_circle_conversion_basic(self):
        for d in self.basic_cases:
            byte_str = nvjson.dumps(d)
            conversed = nvjson.loads(byte_str)

            print("Actual dict: " + str(d))
            print("Conversed dict: " + str(conversed))

            self.assertEqual(sorted(d.items()), sorted(conversed.items()))


if __name__ == '__main__':
    unittest.main()