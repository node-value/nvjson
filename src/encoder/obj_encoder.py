from encoder import primitive_encoder as pe
from common.constants import Tags


def __wrap_dict_values(d: dict):
    return {k: [v] for k, v in d.items()}


def __unwrap_dict_values(d: dict):
    return {k: v[0] for k, v in d.items()}


def __combine_maps(compressed_map, current_map):
    return {k: compressed_map[k] + [v] for k, v in current_map.items()}


def __encode_compressed_dicts(entries_map: dict):
    result = b''
    for _, pair in entries_map.items():
        key_l, compressed_map = pair
        if len(key_l) == 1:
            result += pe.encode_key(key_l[0]) + __choose_encoder(__unwrap_dict_values(compressed_map))
        else:
            result += pe.encode_compound_key(pair[0]) + Tags.OBJ_COMPRESSED + __choose_encoder(pair[1])
    return result


def __encode_compressed_dicts_without_keys(entries_map: dict):
    result = b''
    for _, compressed_map in entries_map.items():
        if len(compressed_map[list(compressed_map.keys())[0]]) == 1:
            result += __choose_encoder(__unwrap_dict_values(compressed_map))
        else:
            result += Tags.OBJ_COMPRESSED + __choose_encoder(compressed_map)
    return result


def __encode_dict(d: dict):
    result = Tags.OBJ_OPEN
    entries_map = {}
    for key, value in d.items():
        if isinstance(value, dict):
            keys_str = str(value.keys())
            if keys_str not in entries_map:
                entries_map[keys_str] = ([key], __wrap_dict_values(value))
            else:
                key_list, compressed_map = entries_map.get(keys_str)
                key_list.append(key)
                compressed_map = __combine_maps(compressed_map, value)
                entries_map[keys_str] = (key_list, compressed_map)

        else:
            result += pe.encode_key(str(key)) + __choose_no_dict_encoder(value)

    return result + __encode_compressed_dicts(entries_map) + Tags.OBJ_CLOSE


def __encode_list(l: list):
    result = Tags.ARR_OPEN
    entries_map = {}
    for item in l:
        if type(item) == type({}):
            keys_str = str(item.keys())

            if keys_str not in entries_map:
                entries_map[keys_str] = __wrap_dict_values(item)
            else:
                entries_map[keys_str] = __combine_maps(entries_map.get(keys_str), item)

        else:
            result += __choose_no_dict_encoder(item)
    return result + __encode_compressed_dicts_without_keys(entries_map) + Tags.ARR_CLOSE


__encoders_map = {
    type(""): lambda x: pe.encode_str(x),
    type(False): lambda x: pe.encode_bool(x),
    type(1): lambda x: pe.encode_integer(x),
    type(None): lambda _: pe.encode_none(),
    type({}): lambda x: __encode_dict(x),
    type([]): lambda x: __encode_list(x)
}

__encoders_no_dict_map = {
    type(""): lambda x: pe.encode_str(x),
    type(False): lambda x: pe.encode_bool(x),
    type(1): lambda x: pe.encode_integer(x),
    type(None): lambda _: pe.encode_none(),
    type([]): lambda x: __encode_list(x)
}


def __choose_encoder(obj):
    return __encoders_map.get(type(obj))(obj)


def __choose_no_dict_encoder(obj):
    return __encoders_no_dict_map.get(type(obj))(obj)


def encode(obj):
    return __choose_encoder(obj)
