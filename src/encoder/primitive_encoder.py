import struct
from common.constants import Tags, Boundaries, StructFormat


def encode_none():
    return Tags.NONE


def encode_bool(boolean):
    return Tags.TRUE if boolean else Tags.FALSE


def encode_str(string):
    encoded_str = string.encode('utf-8')
    return Tags.STR + encode_integer(len(encoded_str)) + encoded_str


def encode_key(key):
    key_str = str(key)
    encoded_str = key_str.encode('utf-8')
    size = len(encoded_str)
    if size > Boundaries.BYTE_MAX:
        print(f"To long key {key}, unable to encode")
        return
    return encode_integer(size) + encoded_str


def encode_compound_key(key_l: list):
    result = Tags.KEY_COMPOUND + encode_integer(len(key_l))
    for key in key_l:
        result += encode_key(key)
    return result


def encode_integer(val):
    if Boundaries.BYTE_MIN <= val <= Boundaries.BYTE_MAX:
        return Tags.BYTE + struct.pack(StructFormat.BYTE, val)
    elif Boundaries.SHORT_MIN <= val <= Boundaries.SHORT_MAX:
        return Tags.SHORT + struct.pack(StructFormat.SHORT, val)
    elif Boundaries.INT_MIN <= val <= Boundaries.INT_MAX:
        return Tags.INT + struct.pack(StructFormat.INT, val)
    elif Boundaries.LONG_MIN <= val <= Boundaries.LONG_MAX:
        return Tags.LONG + struct.pack(StructFormat.LONG, val)
    else:
        print(f"Unable to encode value: {val}")  # TODO Throw an error
