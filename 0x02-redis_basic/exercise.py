#!/usr/bin/env python3
""" Redis basic """
import uuid
import redis
from typing import Union


class Cache:
    """Create a Cache class"""

    def __init__(self):
        """initialize the cache"""
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: Union[str, bytes, int]) -> str:
        """generate a random key store the input data"""
        rand_key = str(uuid.uuid())
        _redis.set(rand_key, data)
