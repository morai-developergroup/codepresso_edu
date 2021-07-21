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


status_port =params["vehicle_status_dst_port"]

class get_status :

    def __init__(self):
        self.status=udp_parser(user_ip, status_port,'status')
        self.main_loop()                

        
    
    def main_loop(self):
        
        os.system('cls')
        self.timer=threading.Timer(1,self.main_loop)
        self.timer.start()
        
        status_data=self.status.get_data()
        position_x=status_data[4]
        position_y=status_data[5]
        position_z=status_data[6]
        heading=status_data[9]
        velocity=status_data[10]
        
        print('--------------------status-------------------------')
        print('ctrl Mode :{}'.format(status_data[0]))
        print('Gear :{}'.format(status_data[1]))
        print('signed velocity :{}'.format(status_data[2]))
        print('Map data id :{}'.format(status_data[3]))
        print('position :{0} ,{1}, {2}'.format(position_x,position_y,position_z))
        print('velocity :{} km/h'.format(velocity,heading))
        print('heading :{} deg'.format(heading))
        
        


if __name__ == "__main__":
    test=get_status()

 








