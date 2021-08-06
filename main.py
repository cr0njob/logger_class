#!/usr/bin/env python
from logger import Logger
from pack_1 import mod_1

if __name__ == '__main__':
    new_logger = Logger(
        name=__name__,
        log_level=20,
        log_to_file=True,
        file_mode='w',
    )

    logger = new_logger.get_logger()

    logger.info('this is a test')

    mod_1.test_func()
