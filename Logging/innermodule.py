import logging

innerlogger = logging.getLogger('multi_module.innermodule')

innerlogger.warning('inner module warning')

print('INNER MODULE')

def some_function():
    innerlogger.error('received a call to "some_function"')