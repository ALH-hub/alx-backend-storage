#!/usr/bin/env python3
"""redis basics"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """initialize redis connection and flush the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key and store the data in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
