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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, last_item = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            return self.cache_data.get(key)
