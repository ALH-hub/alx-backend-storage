#!/usr/bin/env python3
"""list all documents in collection"""
import pymongo


def list_all(mongo_collection):
    """list all documents in collection"""
    return mongo_collection.find()
