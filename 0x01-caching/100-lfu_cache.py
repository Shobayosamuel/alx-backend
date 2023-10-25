#!/usr/bin/python3
"""LFUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """caching system using MRU"""
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)  # Dictionary to track usage frequency
        self.order = {}  # Dictionary to track the order of usage

    def put(self, key, item):
        """put in a value to a key"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item (LFU)
                min_frequency = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_frequency]

                if len(lfu_keys) > 1:
                    # If there's a tie, use LRU to break it
                    lru_key = min(self.order, key=self.order.get)
                    lfu_keys.remove(lru_key)
                else:
                    lru_key = lfu_keys[0]

                print(f"DISCARD: {lru_key}\n")
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.order[lru_key]

            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order[key] = len(self.order)

    def get(self, key):
        """Method to retrieve a value for the key"""
        if key is not None:
            if key in self.cache_data:
                self.order[key] += 1
                return self.cache_data.get(key)
