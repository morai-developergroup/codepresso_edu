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


get_traffic_port=params["get_traffic_dst_port"]


class object_info :

    def __init__(self):

        self.traffic=udp_parser(user_ip, get_traffic_port,'get_traffic')
        self.main_loop()                
       
    
    def main_loop(self):
        
        os.system('cls')
        self.timer=threading.Timer(1,self.main_loop)
        self.timer.start()
    
        traffic_data = self.traffic.get_data()
        print('--------------------trafficLight-------------------------')
        if len(traffic_data) ==4:
            print('traffic mode : {}'.format(traffic_data[0]))
            print('traffic index : {}'.format(traffic_data[1]))
            print('traffic type : {}'.format(traffic_data[2]))
            print('traffic status : {}'.format(traffic_data[3]))


if __name__ == "__main__":

  test=object_info()

 








