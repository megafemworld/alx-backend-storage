#!/usr/bin/env python3
""" Redis basic """
import uuid
import redis
from typing import Union


class Cache:
    """Create a Cache class"""

    def __init__(self):
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key store the input data"""
        rand_key : str = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def fn(value):
        """convert to utf-8"""
        return value.decode('utf-8')

    @property
    def get(self, key, fn=None):
        """convert the data back to the desired format."""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """get a string"""
        return self.decode("utf-8")
