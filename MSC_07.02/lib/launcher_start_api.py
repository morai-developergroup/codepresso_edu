#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,os

from lib.define import *
from lib.read_text import * 

from lib.controller import *


class launcher_start(controller):
        
    def __init__(self):                
        self.controller = controller()

    def launcher_start(self):
        
        while True:
            
            if self.controller.update():             
                self.controller.is_waitting() #status_wait 
                self.controller.is_downloading() #check_is_download_status                                      

                if self.controller.is_befor_login():
                                        
                    self.controller.commander(Command.LOGIN,user_id+'/'+user_pw)#Login명령
                    
                
                if self.controller.is_after_login() or self.controller.is_after_sim_quit_to_launcher():  # is_after_sim_quit_to_launcher : Simulator에서 quit 명령 후 Launcher 복귀 상태 확인

                    self.controller.commander(Command.SELECT_VER,version)#version select명령

                if self.controller.is_not_find_version(): #version_error         
                    break
                    
                if self.controller.is_can_execute_sim(): 
                                                                    
                    self.controller.commander(Command.EXECUTE_SIM,'') #Simulator 실행 명령                        

                    self.controller.watting_execute()
                                            
                if self.controller.is_sim_not_install():                                
                    self.controller.commander(Command.INSTALL_SIM,'') #Simulator 설치 명령         

                if self.controller.is_sim_lobby():                    

                    self.controller.commander(Command.MAP_VEHICLE_SELECT,map+'/'+vehicle)#시뮬레이션/옵션 변경 실행 명령

                    self.controller.watting_loading()

                if self.controller.is_sim_playing():          

                    self.controller.commander(Command.NET_SETTING,network_file) #Network setting
                    
                    self.controller.commander(Command.SEN_SETTING,sensor_file) #Sensor setting

                    self.controller.commander(Command.SCEN_SETTING,scenario_file+"/30") #Scenraio setting
                    '''
                        Scenario option
                        0x01 : Delete All
                        0x02 : Ego Vehicle
                        0x04 : Surround Vehicle
                        0x08 : Pedestrian
                        0x10 : Obstacle
                        0x20: Pause
                        원하는 option을 or 연산 해서 사용 e.g) 0x02 | 0x04 | 0x08 | 0x10  = 0b0010 | 0b0100 | 0b1000 | 0b0001 0000| = 30 (0b0001 1110, 0x1E)
                    '''

                    break

            else :
                print("[NO Simulator Control Data]")
                time.sleep(1)            


    def MAP_VEHICLE_SELECT(self):
        self.controller.commander(Command.MAP_VEHICLE_SELECT, 'R_KR_PG_K-City/2017_Kia_Niro(HEV)') 


    def SIM_PAUSE(self):        
        self.controller.commander(Command.SIM_PAUSE,'')

    def SIM_PLAY(self):            
            self.controller.commander(Command.SIM_PLAY, '') 

    def NET_SETTING(self):            
            self.controller.commander(Command.NET_SETTING, 'msc_test_net_file') 

    def NET_SAVE(self):            
            self.controller.commander(Command.NET_SAVE, 'msc_test_net_file')  
            

    def SEN_SETTING(self):            
            self.controller.commander(Command.SCEN_SETTING, 'test'+"/30") 

    def SEN_SAVE(self):
            
            self.controller.commander(Command.SEN_SAVE, 'test') 

    def SCEN_SETTING(self,file_name):
            self.controller.commander(Command.SCEN_SETTING, file_name+"/30") 

    def SCEN_SAVE(self,file_name):
                        
            self.controller.commander(Command.SCEN_SAVE, file_name) 

    def QUIT_SIM(self):
            self.controller.commander(Command.QUIT_SIM, '') 
