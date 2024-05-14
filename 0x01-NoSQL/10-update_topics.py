#!/usr/bin/env python3
"""update documents in a collection"""


def update_topics(mongo_collection, name, topics):
    """update documents in a collection"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
