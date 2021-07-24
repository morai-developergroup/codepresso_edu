#!/usr/bin/env python
# -*- coding: utf-8 -*-
  

from lib.morai_udp_parser import udp_parser,udp_sender
from lib.utils import pathReader,findLocalPath,purePursuit,Point,cruiseControl,vaildObject,velocityPlanning,pidController
import time
import threading
from math import cos,sin,sqrt,pow,atan2,pi
import os,json


path = os.path.dirname( os.path.abspath( __file__ ) )
with open(os.path.join(path,("params.json")),'r') as fp :
    params = json.load(fp)

params=params["params"]
user_ip = params["user_ip"]
host_ip = params["host_ip"]

set_traffic_port=params["set_traffic_host_port"]





class set_traffic_light :

    def __init__(self):
        self.set_traffic=udp_sender(host_ip,set_traffic_port,'set_traffic')    
        self.main_loop()                
  
    
    def main_loop(self):
        self.timer=threading.Timer(1,self.main_loop)
        self.timer.start()
               
        traffic_id='C119BS010021'
        traffic_status=1
        self.set_traffic.send_data([False,traffic_id,traffic_status])
        

if __name__ == "__main__":


    test=set_traffic_light()

 








