import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-log","--log", help="provide client argument")

log_level = parser.parse_args().log

logging.basicConfig(filename='loggercli.log', encoding='utf-8', level=log_level)
logging.getLogger(__name__)

logging.info('Log starts here')

def main():
    print('Hello Guys')
    logging.warning('warning message logged here')


if __name__ == '__main__':
    main()