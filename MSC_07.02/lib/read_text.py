#!/usr/bin/env python
# -*- Encoding: utf-8 -*-
file = open('params.txt', 'r')
line=file.read()
params=line.split('\n')
for i in range(0,12):
    if params[i].find('\r'):
        params[i]=(params[i].split(':')[1].replace(" ","")).replace("\r","")
    else:
        params[i]=params[i].split(':')[1].replace(" ","")

recive_user_ip = params[0]
recive_user_port = int(params[1])

request_dst_ip = params[2]
request_dst_port = int(params[3])
user_id = params[4]
user_pw = params[5]
version=params[6]
map = params[7]
vehicle = params[8]
network_file = params[9]
sensor_file = params[10]
scenario_file = params[11]