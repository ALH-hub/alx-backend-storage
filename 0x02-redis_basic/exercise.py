#!/usr/bin/env python3
"""redis basics"""

import redis
import uuid
from functools import wraps
from typing import Any, Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """decorator to count the number of calls to a function"""
    func = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper function"""
        self._redis.incr(func)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        """initialize redis connection and flush the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key and store the data in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """get the data from redis and apply the function if it exists"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, val: bytes) -> str:
        """return string representation of val from get method """
        return val.decode('utf-8')

    def get_int(self, val: bytes) -> int:
        """return integer representation of val from get method """
        return int.from_bytes(val, byteorder='big')
