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


object_port =params["object_info_dst_port"]




class object_info :

    def __init__(self):

        self.obj=udp_parser(user_ip, object_port,'obj')
        self.main_loop()                
       
    
    def main_loop(self):
        
        os.system('cls')
        self.timer=threading.Timer(1,self.main_loop)
        self.timer.start()
    
        obj_data=self.obj.get_data()
        print('--------------------object-------------------------')
        print('object num :{}'.format(len(obj_data)))
        for i,obj_info in enumerate(obj_data) :
            print('{0} : type = {1}, x = {2}, y = {3}, z = {4}  heading = {5} , velocity = {6}'.format(i,obj_info[0],obj_info[1],obj_info[2],obj_info[3],obj_info[4],obj_info[8]))

     


if __name__ == "__main__":

  test=object_info()

 








