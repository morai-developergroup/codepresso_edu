#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
from lib.controller import *
from lib.launcher_start_api import *
from lib.read_text import *

class api :

    def __init__(self):         
        
        api = launcher_start()

        # api.launcher_start()                                              
        api.SCEN_SETTING('abc')

if __name__ == "__main__":
    start=api()
    