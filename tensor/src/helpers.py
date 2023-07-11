from typing import NamedTuple, Dict, Union, List
from dataclasses import dataclass
import hashlib
import time
import tracemalloc
import math

class DType(NamedTuple):
    name: str
    size: int

TensorData = Dict[str, Dict[str, Union[DType, List[int], bytes]]]
ModelData = Dict[str, Dict[str, Union[DType, List[int]]]]

def prod(x): return math.prod(x)

def gen_file_name(name: str, shape, dtype: str) -> str:
    shape = shape if isinstance(shape, tuple) else tuple(shape)
    m = hashlib.sha256()
    m.update(f"{name}{str(shape)}{dtype}".encode("utf-8"))
    return str(m.hexdigest())

class Timer(object):
    def __init__(self, prefix=""): self.prefix = prefix
    def __enter__(self): 
        self.st = time.perf_counter_ns()
        tracemalloc.start()
    def __exit__(self, xt, xv, xtb): 
        print(f"{self.prefix} {(time.perf_counter_ns() - self.st)*1e-6:.2f} ms using {tracemalloc.get_traced_memory()[1]*1e-6:.2f} MB")
        tracemalloc.stop()
@dataclass
class dtypes:
    @staticmethod
    def from_str(x: str) -> DType: return getattr(dtypes, x)

    float32 = DType("float32", 4)
    float16 = DType("float16", 2)
    bfloat16 = DType("bfloat16", 2)
    int32 = DType("int32", 4)
    int16 = DType("int16", 2)
    int8 = DType("int8", 1)
    uint8 = DType("uint8", 1)
    int64 = DType("int64", 8)
