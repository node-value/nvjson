class Boundaries:
    BYTE_MIN = -2 ** 7
    BYTE_MAX = 2 ** 7 - 1

    SHORT_MIN = -2 ** 15
    SHORT_MAX = 2 ** 15 - 1

    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    LONG_MIN = -2 ** 63
    LONG_MAX = 2 ** 63 - 1


class Tags:
    BYTE = b'i'
    SHORT = b'I'
    INT = b'l'
    LONG = b'L'
    INTEGER_LIST_SIZES = {BYTE: 1, SHORT: 2, INT: 4, LONG: 8}

    FLOAT = b'd'
    DOUBLE = b'D'

    STR = b'S'
    TRUE = b'T'
    FALSE = b'F'
    NONE = b'N'
    KEY_COMPOUND = b'K'

    OBJ_OPEN = b'{'
    OBJ_CLOSE = b'}'

    OBJ_COMPRESSED = b'C'

    ARR_OPEN = b'['
    ARR_CLOSE = b']'


class StructFormat:
    BYTE = '>b'
    SHORT = '>h'
    INT = '>i'
    LONG = '>q'
    FLOAT = '>f'
    DOUBLE = '>d'
    STR = '>s'
