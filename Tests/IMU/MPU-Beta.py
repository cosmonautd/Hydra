## Hydra MPU Code V0.01

from mpu6050 import mpu6050 #Package https://github.com/Tijndagamer/mpu6050.
import time                 #Package to use the pause function in code.
from math import *          #Package mathematics for the use of physics calculus


mpu = mpu6050(0x68)         #The address function for sensor use.
print(mpu.get_temp())       #Temperature return in celsius. 
Err_acc = 0.3               #Error rate for acceleration values.
Wait_time = 0.2             #Waiting time for reading date.

###** TODO **
# Implementation of the function speed instantaneous;
# Check date Erro in real car Hydra;

#def vel_int(ac_x, ac_y, time)
#    Vx = Vx0 - a*(Wait_time)
#    return V(x,y)

try: #Interruption Structure
    while True:
        time.sleep(Wait_time) # dalay in time of the read.
        accel_data = mpu.get_accel_data()
        if (abs(accel_data['x']) or abs(accel_data['y'])) >= Err_acc:
            print("\n Estou em movimento: a em x: %f y: %f \n" %(accel_data['x'], accel_data['y']))
        else:
            print("\n Estou parado \n")
except KeyboardInterrupt: #Interruption Structure
    pass
    