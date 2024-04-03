from common.constants import Tags
import decoder.primitive_decoder as pd
import decoder.tokenizer as t


def decode(data):
    decoder = __Decoder(data)
    return decoder.decode()


class __Decoder:

    def __init__(self, data):
        self._data = data

    def __skip_byte(self):
        self._data = self._data[1:]

    def __decode_compound_key(self):
        result = []
        self.__skip_byte()
        (int_token, self._data) = t.tokenize_integer(self._data)
        for _ in range(pd.decode_integer(int_token)):
            (key_token, self._data) = t.tokenize_key(self._data)
            result.append(pd.decode_key(key_token))

        return result

    def __decode_dict(self):
        result = {}
        self.__skip_byte()
        while self._data[0:1] != Tags.OBJ_CLOSE:
            if self._data[0:1] == Tags.KEY_COMPOUND:
                key_list = self.__decode_compound_key()
                self.__skip_byte()
                compressed_dict = self.__decode_dict()
                for i in range(len(key_list)):
                    result[key_list[i]] = self.__extract_dict_slice(compressed_dict, i)
            else:
                (key_token, self._data) = t.tokenize_key(self._data)
                result[pd.decode_key(key_token)] = self.__choose_decoder()
        self.__skip_byte()
        return result

    def __decode_list(self):
        result = []
        self.__skip_byte()
        while self._data[0:1] != Tags.ARR_CLOSE:
            if self._data[0:1] == Tags.OBJ_COMPRESSED:
                self.__skip_byte()
                compressed_dict = self.__decode_dict()
                for i in range(len(compressed_dict[list(compressed_dict.keys())[0]])):
                    result.append(self.__extract_dict_slice(compressed_dict, i))
            else:
                result.append(self.__choose_decoder())
        self.__skip_byte()
        return result

    def __extract_dict_slice(self, compressed_dict, i):
        return {k: v[i] for k, v in compressed_dict.items()}

    def __decompress_dict(self, key_list, compressed_dict):
        return {key_list[i]: self.__extract_dict_slice(compressed_dict, i) for i in range(len(key_list))}

    def __choose_decoder(self):
        tag = self._data[0:1]
        match tag:
            case Tags.OBJ_OPEN:
                return self.__decode_dict()
            case Tags.ARR_OPEN:
                return self.__decode_list()
            case Tags.FALSE | Tags.TRUE:
                (boolean_token, self._data) = t.tokenize_byte(self._data)
                return pd.decode_bool(boolean_token)
            case Tags.NONE:
                (_, self._data) = t.tokenize_byte(self._data)
                return pd.decode_none()
            case Tags.BYTE | Tags.SHORT | Tags.INT | Tags.LONG:
                (integer_token, self._data) = t.tokenize_integer(self._data)
                return pd.decode_integer(integer_token)
            case Tags.STR:
                (str_token, self._data) = t.tokenize_str(self._data)
                return pd.decode_str(str_token)
            case _:
                print(f"Unexpected tag: {tag}, unable to decode")

    def decode(self):
        return self.__choose_decoder()
