import logging
import innermodule

logger = logging.getLogger('multi_module')
logger.setLevel(logging.DEBUG)


h1 = logging.FileHandler('multi_module.log')
h1.setLevel(logging.INFO)

h2 = logging.StreamHandler()
h2.setLevel(logging.ERROR)

formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

h1.setFormatter(formatter)
h2.setFormatter(formatter)

logger.addHandler(h1)
logger.addHandler(h2)


logger.debug('Debug message')
logger.info('Information message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical error')
innermodule.some_function()
