from decoder import primitive_decoder
from common.constants import Tags


def tokenize_key(data):
    number_byte_size = Tags.INTEGER_LIST_SIZES.get(data[0:1])
    key_len = primitive_decoder.decode_integer(data[0:1 + number_byte_size])
    token_len = 1 + number_byte_size + key_len
    return data[0:token_len], data[token_len:]


def tokenize_str(data):
    data_without_str_tag = data[1:]
    number_byte_size = Tags.INTEGER_LIST_SIZES.get(data_without_str_tag[0:1])
    str_len = primitive_decoder.decode_integer(data_without_str_tag[0:1 + number_byte_size])
    token_len = 2 + number_byte_size + str_len
    return data[0:token_len], data[token_len:]


def tokenize_integer(data):
    number_byte_size = Tags.INTEGER_LIST_SIZES.get(data[0:1])
    token_len = 1 + number_byte_size
    return data[0:token_len], data[token_len:]


def tokenize_byte(data):
    return data[0:1], data[1:]
