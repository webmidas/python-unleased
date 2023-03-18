import logging

logging.getLogger(__name__)

logging.info('Log starts here')

def main():
    print('Hello Guys')
    logging.warning('warning message logged here')


if __name__ == '__main__':
    main()