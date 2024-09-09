#!/usr/bin/env python3
"""
Web cache and tracker
"""
import requests
import redis
from functools import wraps

# Connect to Redis (adjust the host and port if necessary)
store = redis.Redis(host='localhost', port=6379, db=0)

def count_url_access(method):
    """Decorator counting how many times a URL is accessed and caching results."""
    @wraps(method)
    def wrapper(url: str):
        # Generate Redis keys for caching and counting
        cached_key = f"cached:{url}"
        count_key = f"count:{url}"
        
        # Check if the result is in the cache
        cached_data = store.get(cached_key)
        if cached_data:
            # Increment the access count
            store.incr(count_key)
            return cached_data.decode("utf-8")

        # If not cached, call the actual method
        html = method(url)

        # Cache the result with expiration
        store.setex(cached_key, 10, html)
        # Increment the access count
        store.incr(count_key)
        
        return html
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """Fetches the HTML content of the given URL."""
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors
        return res.text
    except requests.RequestException as e:
        # Handle request errors (e.g., network problems, invalid URLs)
        print(f"Error fetching {url}: {e}")
        return ""

if __name__ == "__main__":
    # Example usage (optional, for testing purposes)
    test_url = "http://slowwly.robertomurray.co.uk"
    print(get_page(test_url))
