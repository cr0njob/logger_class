#!/usr/bin/env python
from pprint import pformat

def log_struct(logger, struct):
    f = pformat(struct, width=80)
    for line in f.splitlines():
        logger.info(line)
