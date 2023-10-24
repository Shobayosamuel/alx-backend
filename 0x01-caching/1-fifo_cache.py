#!/usr/bin/python3
"""FIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching system using FIFO"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method to put a key-value pair using FIFO method of caching"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            return self.cache_data.get(key)
