
import logging


logging.basicConfig(filename='module.log', encoding='utf-8',format='%(asctime)s %(levelname)s:%(name)s:%(message)s', datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.DEBUG)
logger = logging.getLogger(__name__)
import custom_lib
logger.info('Log starts here')

def main():
    print('Hello Guys')
    logger.warning('warning message logged here')
    custom_lib.custom_activity()
    logger.info('custom activity finished')


if __name__ == '__main__':
    main()