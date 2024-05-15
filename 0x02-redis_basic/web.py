import requests
from typing import Callable, Union
import redis
from functools import wraps
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data, ex=10)
        return random_key

    def get(self, key: str) -> Union[str, bytes, int, float]:
        return self._redis.get(key)

    def increment(self, key: str) -> None:
        self._redis.incr(key)


cache = Cache()


def cache_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        cached_result = cache.get(url)
        if cached_result is not None:
            return cached_result

        result = func(url)
        cache.store(url, result)
        cache.increment(f"count:{url}")
        return result

    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """returns the HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
