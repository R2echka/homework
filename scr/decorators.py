from typing import Optional, Callable, Any

def log(filename: Optional[str]=None) -> Callable:
    def dec(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> str:
            try:
                func(*args, **kwargs)
                result = f'{func.__name__} ok'
            except Exception as e:
                result = f'{func.__name__} error: {type(e).__name__}. Inputs: {(args)}, {kwargs}'
            if filename:
                with open(filename, 'a') as f:
                    f.write(result, '\n')
            else:
                print(result)
            return result
        return wrapper
    return dec

@log()
def idk(first, sec):
    return first/sec

a = idk(4, 2)
b = idk(0, 5)
c = idk(1, 0)