import functools

def log_method_call(method):
    """Декоратор для логирования вызовов метода."""
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print(f"Calling method: {method.__name__} with args: {args} and kwargs: {kwargs}")
        return method(*args, **kwargs)
    return wrapper

def validate_positive_numbers(method):
    """Декоратор для проверки, что входные параметры положительны."""
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'mass' in kwargs and kwargs['mass'] <= 0:
            raise ValueError("Mass must be a positive number.")
        if 'charge' in kwargs and kwargs['charge'] <= 0:
            raise ValueError("Charge must be a positive number.")
        return method(*args, **kwargs)
    return wrapper

def cache_result(method):
    """Декоратор для кэширования результатов."""
    cache = {}

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = method(*args, **kwargs)
        return cache[key]
    return wrapper