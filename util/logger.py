import logging
from logging import Logger as PythonLogger
from typing import Callable
from functools import wraps

class Logger:

    def __init__(self):
        self.__logger = logging.getLogger("MyApp")
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(funcName)s::%(lineno)d - %(message)s'
        logging.basicConfig(filename="my_app.log", level=logging.DEBUG, format=formatter)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            print('new instance')
        return cls.instance
    
    def get_logger(self) -> PythonLogger:
        return self.__logger
    
def enable_logging(function_pointer:Callable):
    @wraps(function_pointer)
    def wrapper(*args, **kwargs):
        Logger().get_logger().info(f'Begin: {function_pointer.__name__}')
        Logger().get_logger().info(f'[{args}] -- [{kwargs}]')
        try:
            result = function_pointer(*args, **kwargs)
        except Exception as ex:
            Logger().get_logger().error(ex, exc_info=True)
            raise ex
        Logger().get_logger().info(f'End: {function_pointer.__name__}')
        return result
    return wrapper