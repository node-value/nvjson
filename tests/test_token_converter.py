import unittest
from encoder import primitive_encoder
from decoder import primitive_decoder
from common.constants import Boundaries


class TestConverter(unittest.TestCase):
    def test_encode_key(self):
        encoded_key = primitive_encoder.encode_key("test_key")
        self.assertIsNotNone(encoded_key)

    def test_decode_key(self):
        key_byte = b'i\x04' + "test".encode()
        decoded_key = primitive_decoder.decode_key(key_byte)
        self.assertEqual(decoded_key, "test")

    def test_circle_conversion_key(self):
        test_string = "test_string"
        circled_string = primitive_decoder.decode_key(primitive_encoder.encode_key(test_string))
        self.assertEqual(test_string, circled_string)

    def test_encode_integer(self):
        encoded_integer = primitive_encoder.encode_integer(42)
        self.assertIsNotNone(encoded_integer)

    def test_decode_integer(self):
        encoded_integer = b'l\x00\x05\x16\x15'
        decoded_integer = primitive_decoder.decode_integer(encoded_integer)
        self.assertEqual(decoded_integer, 333333)

    def test_circle_conversion_integer(self):
        n = 1111111111111
        circled_n = primitive_decoder.decode_integer(primitive_encoder.encode_integer(n))
        self.assertEqual(n, circled_n)

    def test_circle_conversion_byte_string(self):
        test_str = "g" * Boundaries.BYTE_MAX
        circled_str = primitive_decoder.decode_str(primitive_encoder.encode_str(test_str))
        self.assertEqual(test_str, circled_str)

    def test_circle_conversion_short_string(self):
        test_str = "g" * Boundaries.SHORT_MAX
        circled_str = primitive_decoder.decode_str(primitive_encoder.encode_str(test_str))
        self.assertEqual(test_str, circled_str)

    def test_circle_conversion_int_string(self):
        test_str = "g" * Boundaries.INT_MAX
        circled_str = primitive_decoder.decode_str(primitive_encoder.encode_str(test_str))
        self.assertEqual(test_str, circled_str)

    def test_circle_conversion_boolean(self):
        boolean = True
        circled_boolean = primitive_decoder.decode_bool(primitive_encoder.encode_bool(boolean))
        self.assertEqual(boolean, circled_boolean)


if __name__ == '__main__':
    unittest.main()
