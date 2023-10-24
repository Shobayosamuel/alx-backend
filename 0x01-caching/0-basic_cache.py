#!/usr/bin/python3
"""BasicCache class that inherits from BaseCaching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache for get and put methods"""
    def put(self, key, item):
        """Method to put a key-value pair"""
        if key is not None and item is not None:
            self.cache_data = {key: item}

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            return self.cache_data.get(key)
