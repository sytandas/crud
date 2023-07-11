import os
from collections import defaultdict
import ctypes
from typing import Union, List, Dict
from helpers import gen_file_name, DType, ModelData, TensorData, dtypes

import torch
import numpy as np

torch_dtypes = {
    torch.float32: dtypes.float32, 
    torch.float16: dtypes.float16, 
    torch.bfloat16: dtypes.bfloat16, 
    torch.int32: dtypes.int32, 
    torch.int: dtypes.int32, 
    torch.int16: dtypes.int16, 
    torch.int64: dtypes.int64, 
    torch.int8: dtypes.int8,
    torch.uint8: dtypes.uint8,
}
torch_dtypes_inv = {v:k for k,v in torch_dtypes.items()}

def flatten_torch(tensors: Dict[str, torch.Tensor]) -> TensorData:
    assert all(isinstance(v, torch.Tensor) for v in tensors.values())
    ptrs = defaultdict(set)
    [ptrs[torch.storage_ptr(v)].add(k) for k,v in tensors.items() if v.layout != torch.strided]        
    if len([x for x in ptrs.values() if len(x) > 1]) > 0: raise RuntimeError("Tensors with same storage found")
    return { k: { "dtype": conv_dtype_torch(v.dtype), "shape": tuple(v.shape), "data": _bytes_from_torch(v), } for k, v in tensors.items() }

def conv_dtype_torch(dtype: torch.dtype) -> DType:
    return torch_dtypes[dtype]

def _bytes_from_torch(tensor: torch.Tensor) -> bytes:
    if tensor.device.type != "cpu":
        tensor = tensor.to("cpu")
    ptr = tensor.data_ptr()
    tb = int(np.prod(tensor.shape).item()) * conv_dtype_torch(tensor.dtype).size
    return np.ctypeslib.as_array(ctypes.cast(ptr, ctypes.POINTER(ctypes.c_byte)), shape=(tb,)).tobytes() if ptr != 0 else b""

def model_data_torch(path: str, data: ModelData) -> Dict[str, torch.Tensor]:
    return {k: create_tensor_torch(v["dtype"], v["shape"], os.path.join(path, gen_file_name(k, v["shape"], v["dtype"].name) + ".⚡")) for k, v in data.items()} # TODO: add data loader.

def create_tensor_torch(dtype: DType, shape: List[int], path: str) -> torch.Tensor:
    with open(path, "r+b") as f:
        return torch.frombuffer(bytearray(f.read()), dtype=torch_dtypes_inv[dtype]).reshape(shape)

def load_files_torch(files: Union[str,List[str]], map_location="cpu") -> Dict[str, torch.Tensor]:
    if isinstance(files, str):
        files = [files]
    assert len(files) > 0
    res = dict()
    [res.update(torch.load(x, map_location=map_location)) for x in files]
    return res
