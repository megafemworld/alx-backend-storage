#!/usr/bin/env python3
""" Redis basic """
import uuid
import redis
from functools import wraps
from typing import Union, Callable, Optional, Any


def count_calls(method: callable) -> callable :
    """count_calls decorator"""
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """decorator for the decorator"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Create a Cache class"""

    def __init__(self):
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key store the input data"""
        rand_key : str = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key, fn: Optional[Callable]=None):
        """convert the data back to the desired format."""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self, data: bytes) -> int:
        """get a number"""
        return int(data)

    def get_str(self, data: bytes) -> str:
        """get a string"""
        return data.decode("utf-8")
