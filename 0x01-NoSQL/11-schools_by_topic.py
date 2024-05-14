#!/usr/bin/env python3
"""list documents with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """list documents with a specific topic"""
    return mongo_collection.find({"topics": topic})
