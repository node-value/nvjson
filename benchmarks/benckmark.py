import sys
import timeit
import json
import nvjson
from util import json_reader

data = json.loads(json_reader.read_other_cases("citm_catalog.json"))


def benchmark_json():
    return json.dumps(data)


def benchmark_nvjson():
    return nvjson.dumps(data)


json_time = timeit.timeit(benchmark_json, number=100)
nvjson_time = timeit.timeit(benchmark_nvjson, number=100)

json_size = sys.getsizeof(benchmark_json())
nvjson_size = sys.getsizeof(benchmark_nvjson())

print("Time comparison")
print("    json.dumps execution time: {:.6f} seconds".format(json_time))
print("    nvjson.dumps execution time: {:.6f} seconds".format(nvjson_time))
print(f"json.dumps faster {nvjson_time/json_time} times" if json_time < nvjson_time else f"nvjson.dumps faster {json_time/nvjson_time} times")

print()
print("Size comparison")
print("    json.dumps result size:", json_size, "bytes")
print("    nvjson.dumps result size:", nvjson_size, "bytes")
print(f"json.dumps smaller in size {nvjson_size/json_size} times" if json_size < nvjson_size else f"nvjson.dumps smaller in size {json_size/nvjson_size} times")