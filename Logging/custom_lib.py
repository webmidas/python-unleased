import logging

logger = logging.getLogger(__name__)
print(__name__)
logger.info('custom library log here')

def custom_activity():
    print('Custom activity starts here')
    logger.warning('warning for custom activity has occured')


if __name__ == '__main__':
    custom_activity()