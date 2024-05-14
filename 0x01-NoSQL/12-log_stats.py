#!/usr/bin/env python3
"""log stats"""
from pymongo import MongoClient


def log_stats():
    """log stats"""
    client = MongoClient()
    logs = client.logs.nginx
    print(f'{logs.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {logs.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {logs.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {logs.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {logs.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {logs.count_documents({"method": "DELETE"})}')
    print(f'{logs.count_documents({
        "method": "GET",
        "path": "/status"
        })} status check')


log_stats()
