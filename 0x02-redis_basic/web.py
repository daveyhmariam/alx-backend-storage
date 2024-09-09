import requests
import redis
import time
from functools import wraps

# Connect to Redis (adjust the host and port if necessary)
r = redis.Redis(host='localhost', port=6379, db=0)

def cache_with_tracking(expiration=10):
    """Decorator to cache the result of a function and track URL access count."""
    def decorator(func):
        @wraps(func)
        def wrapper(url, *args, **kwargs):
            # Key to track the access count
            count_key = f"count:{url}"
            # Key to cache the result
            cache_key = f"cache:{url}"
            
            # Check if the result is in the cache
            cached_result = r.get(cache_key)
            if cached_result:
                # Increment the access count
                r.incr(count_key)
                # Return the cached result
                return cached_result.decode('utf-8')
            
            # If not cached, call the actual function
            result = func(url, *args, **kwargs)
            
            # Cache the result with expiration
            r.setex(cache_key, expiration, result)
            # Increment the access count
            r.incr(count_key)
            
            return result
        return wrapper
    return decorator

@cache_with_tracking(expiration=10)
def get_page(url: str) -> str:
    """Fetches the HTML content of the given URL."""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    # Test the function
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    time.sleep(5)  # Sleep to test caching
    print(get_page(url))
