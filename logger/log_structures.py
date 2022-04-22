#!/usr/bin/env python
import json
import logging

def log_struct(log_obj, d_struct=None):
    log_obj.setLevel(logging.INFO)

    if d_struct:
        for s in [dict, list, tuple]:
            if isinstance(d_struct, s):
                log_obj.info(json.dumps(d_struct, indent=4))
    
