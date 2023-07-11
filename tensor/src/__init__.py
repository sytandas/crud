import os
import toml
import math
from typing import Union
from helpers import dtypes, TensorData, ModelData, gen_file_name

model_name="model.toml"
DEBUG=int(os.getenv("DEBUG", 0))


def load_model_data(_path: str) -> ModelData:
    _path = os.path.join(_path, model_name)
    if not os.path.exists(_path): raise FileNotFoundError(f"[error] {model_name} not found in the specified path")
    with open(_path, "r") as f:
        return {k: {"dtype": dtypes.from_str(v['dtype']), "shape": v['shape']} for k,v in toml.load(f).items()}

def verify_model_files(_path: str, model_data: ModelData):
    file_names = [[os.path.join(_path, gen_file_name(k, tuple(v["shape"]), v["dtype"].name) + ".⚡"), v["dtype"].size * int(math.prod(v["shape"]))] for k, v in model_data.items()]
    failed = dict()
    for [name, size] in file_names: 
        if (err := verify_file(name, size)) is not None: failed[name] = err
    return failed

def verify_file(file_name: str, expected_size: int) -> Union[str, None]:
    if not os.path.exists(file_name): return (f"[error] {file_name} not found in the specified path")
    if os.path.getsize(file_name) != expected_size: return f"[error] {file_name} has an unexpected size"
    return None

def save_data(_out: str, m: TensorData):
    # TODO: make this multi-threaded
    files_to_save = [{"name": gen_file_name(k, v["shape"], v["dtype"].name) + ".⚡", "type": "binary", "data": v["data"]} for k, v in m.items()] + [{"name": model_name, "type": "toml", "data": toml.dumps({ k: { "dtype": v["dtype"].name, "shape": v["shape"] } for k, v in m.items() })}]
    for x in files_to_save:
        if DEBUG >= 1: print(f"[info] saving {x['name']}")
        with open(os.path.join(_out, x["name"]), f"w{'b' if x['type'] == 'binary' else ''}") as f:
            f.write(x["data"])
