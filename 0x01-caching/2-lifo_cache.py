#!/usr/bin/python3
"""LIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """caching system using LIFO"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method to put a key-value pair using LIFO method of caching"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            return self.cache_data.get(key)
