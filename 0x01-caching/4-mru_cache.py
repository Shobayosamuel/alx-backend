#!/usr/bin/python3
"""LRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """caching system using MRU"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method to put a key-value pair using MRU method of caching"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop()
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data.get(key)
