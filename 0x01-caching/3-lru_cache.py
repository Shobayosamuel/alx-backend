#!/usr/bin/python3
"""LRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """caching system using LRU"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method to put a key-value pair using LRU method of caching"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(0)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data.get(key)
