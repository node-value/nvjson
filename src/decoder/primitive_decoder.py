import struct
from common.constants import Tags, StructFormat


def decode_none():
    return None


def decode_bool(data):
    return data[0:1] == Tags.TRUE


def decode_str(data):
    integer_tag = data[1:2]
    return data[2 + Tags.INTEGER_LIST_SIZES.get(integer_tag):].decode('utf-8')


def decode_key(key_byte):
    return key_byte[2:].decode('utf-8')


def decode_integer(data):
    tag = data[0:1]
    if tag == Tags.BYTE:
        return struct.unpack(StructFormat.BYTE, data[1:])[0]
    elif tag == Tags.SHORT:
        return struct.unpack(StructFormat.SHORT, data[1:])[0]
    elif tag == Tags.INT:
        return struct.unpack(StructFormat.INT, data[1:])[0]
    elif tag == Tags.LONG:
        return struct.unpack(StructFormat.LONG, data[1:])[0]
    else:
        print(f"Unable to decode data: {data}")