
from util.logger import Logger

def my_decorator(func):
    def wrapper(*args, **kwargs):
        Logger().get_logger().info(f'Begin: {func.__name__} -- [{args}] -- [{kwargs}]')
        result = func(*args, **kwargs)
        Logger().get_logger().info(f'End: {func.__name__}')
        return result
    return wrapper

def add(*args):
    print(args)
    
@my_decorator
def test(**kwargs):
    print(kwargs)

    
add(1,2,3,4)
print("")
test(v1=1, v2=2)