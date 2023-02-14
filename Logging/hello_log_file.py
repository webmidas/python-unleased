import logging

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger(__name__)

logging.info('Log starts here')

def main():
    print('Hello Guys')
    logging.warning('warning message logged here')


if __name__ == '__main__':
    main()