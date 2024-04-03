import encoder.obj_encoder as encoder
import decoder.obj_decoder as decoder


def dumps(obj):
    return encoder.encode(obj)


def loads(data):
    return decoder.decode(data)
