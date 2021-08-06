#!/usr/bin/env python
from logger import Logger

LOGGER = Logger(
    name=__name__,
    log_level=30,
    log_format='%(levelname)s: %(message)s'
).get_logger()

def test_func():
    LOGGER.warning('this is a warning...')
