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


multi_ego_setting_port =params["multi_ego_host_port"]


class multi_ego_setting :

    def __init__(self):
        self.multi_ego=udp_sender(host_ip,multi_ego_setting_port,'multi_ego')
        self.main_loop() 

    def main_loop(self):
        self.timer=threading.Timer(0.05,self.main_loop)
        self.timer.start()

        multi_ego_data=[]
        ego_0=[0,50.499 ,1150.001,0.0,0.0,0.0,0.0,0.0,0,0]
        multi_ego_data.append(ego_0)
        self.multi_ego.send_data(multi_ego_data)
    

if __name__ == "__main__":
    test=multi_ego_setting()

 
