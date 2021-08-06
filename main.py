#!/usr/bin/env python
from logger import Logger
from logger.log_structures import log_struct
from pack_1 import mod_1

LOGGER = Logger(
        name=__name__,
        log_level=20,
        log_to_file=True,
        file_mode='w',
    ).get_logger()


if __name__ == '__main__':
    data = {
        'first': {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': {
                'nest_1': 'n1',
                'nest_2': 'n2',
                'nest_3': 'n3'
            }
        },
        'second': [
            'list_one',
            'list_two',
            'list_three'
        ],
        'third': (
            'tuple_one',
            'tuple_two'
        )
    }

    log_struct(LOGGER, data)