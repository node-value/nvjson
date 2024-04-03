import unittest
from decoder import tokenizer


class TestTokenizer(unittest.TestCase):
    def test_tokenize_key(self):
        byte_arr = b'i\x04namerest_of_the_data'
        (key_token, data_tail) = tokenizer.tokenize_key(byte_arr)

        self.assertEqual(key_token, b'i\x04name')  # add assertion here
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_str(self):
        byte_arr = b'Si\x04namerest_of_the_data'
        (str_token, data_tail) = tokenizer.tokenize_str(byte_arr)

        self.assertEqual(str_token, b'Si\x04name')  # add assertion here
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_byte(self):
        byte_arr = b'TFNrest_of_the_data'

        (true_token, data_tail) = tokenizer.tokenize_byte(byte_arr)
        self.assertEqual(true_token, b'T')
        self.assertEqual(data_tail, b'FNrest_of_the_data')

        (false_token, data_tail) = tokenizer.tokenize_byte(data_tail)
        self.assertEqual(false_token, b'F')
        self.assertEqual(data_tail, b'Nrest_of_the_data')

        (none_token, data_tail) = tokenizer.tokenize_byte(data_tail)
        self.assertEqual(none_token, b'N')
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_integer_byte(self):
        byte_arr = b'i\x04rest_of_the_data'
        (byte_token, data_tail) = tokenizer.tokenize_integer(byte_arr)

        self.assertEqual(byte_token, b'i\x04')
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_integer_short(self):
        byte_arr = b'I\x7f\xffrest_of_the_data'
        (short_token, data_tail) = tokenizer.tokenize_integer(byte_arr)

        self.assertEqual(short_token, b'I\x7f\xff')
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_integer_int(self):
        byte_arr = b'l\x7f\xff\xff\xffrest_of_the_data'
        (int_token, data_tail) = tokenizer.tokenize_integer(byte_arr)

        self.assertEqual(int_token, b'l\x7f\xff\xff\xff')
        self.assertEqual(data_tail, b'rest_of_the_data')

    def test_tokenize_integer_long(self):
        byte_arr = b'L\x7f\xff\xff\xff\xff\xff\xff\xffrest_of_the_data'
        (long_token, data_tail) = tokenizer.tokenize_integer(byte_arr)

        self.assertEqual(long_token, b'L\x7f\xff\xff\xff\xff\xff\xff\xff')
        self.assertEqual(data_tail, b'rest_of_the_data')


if __name__ == '__main__':
    unittest.main()
