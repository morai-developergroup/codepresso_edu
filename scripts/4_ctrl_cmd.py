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


ctrl_cmd_port = params["ctrl_cmd_host_port"]

class ctrl_cmd :

    def __init__(self):

        self.ctrl_cmd=udp_sender(host_ip,ctrl_cmd_port,'ctrl_cmd')
        self.main_loop()                

        
    
    def main_loop(self):
        
        
        self.timer=threading.Timer(0.05,self.main_loop)
        self.timer.start()
        

        # ctrl_mode 1: Keyboard, 2 : Automode
        ctrl_mode=2
        # gear 1: P, 2 : R, 3 : N, 4 : D
        gear=4
        accel=1.0
        brake=0.0
        # steering angle : 1/36.25 * angle(degree)
        steering_angle=0.0
        self.ctrl_cmd.send_data([ctrl_mode,gear,accel,brake,steering_angle])


if __name__ == "__main__":
    test=ctrl_cmd()









