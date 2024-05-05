import toolbox.printer
from itertools import repeat
import logging
import concurrent.futures
import time

logger = logging.getLogger(__name__)

def _jeje(a):
    time.sleep(a)
    logger.info(f'{a}')
    return a*a


if __name__ == '__main__':
    logger.info("an info")
    logger.warning("a warning")
    nums = [1, 2, 3]
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        threaded_output = list(executor.map(_jeje, nums))
        # for _to in threaded_output:
        #     logger.info(_to)