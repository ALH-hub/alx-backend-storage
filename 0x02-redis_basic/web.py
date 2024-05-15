#!/usr/bin/env python3
"""uses the request module to obtain
the HTML content of a particular URL and returns it
"""
import requests


def get_page(url: str) -> str:
    """returns the HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
