#!/usr/bin/env python3
"""log stats"""
from pymongo import MongoClient


client = MongoClient()
logs = client.logs.nginx

if __name__ == "__main__":
    """log stats"""
    print(f'{logs.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {logs.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {logs.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {logs.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {logs.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {logs.count_documents({"method": "DELETE"})}')
    stats = logs.count_documents({"method": "GET", "path": "/status"})
    print(f'{stats} status check')
    print('IPs:')
    ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')
