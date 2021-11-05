#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#開發人員:Ness_huang
#日期:2021-11-05
#版本號:v1
#
#全域變數global variable
TEMP_01=0; HUMI_01=0; TEMP_02=0; HUMI_02=0;
Oid_list = "TEMP_01/HUMI_01/TEMP_02/HUMI_02"
                       
def __GetSensor__():
    import time
    import board
    import psutil
    import adafruit_dht
    global TEMP_01,HUMI_01,TEMP_02,HUMI_02

###kill processing
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
###GPIO pin
    sensor1 = adafruit_dht.DHT11(board.D23)
    sensor2 = adafruit_dht.DHT11(board.D24)

    while True:
        try:
###DHT模組1
            TEMP_01 = sensor1.temperature
            HUMI_01 = sensor1.humidity
###DHT模組2
            TEMP_02 = sensor2.temperature
            HUMI_02 = sensor2.humidity
                        
            __CreatNewFile__()
            __EditFile__()
#產生+編輯oid-value.py      
        except RuntimeError as error:
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error

        time.sleep(2.0)

#產生oid-value.py
def __CreatNewFile__():
    print("__CreatNewFile__() - 用於產生oid-value.py")
    from pathlib import Path

    myfile = Path('oid-value.py')
    myfile.touch(exist_ok=True)
    f = open(myfile)

def __EditFile__():
    print("__EditFile__() - 用於更新oid-value.py內文")
    path = 'oid-value.py'
    f = open(path, 'w')
    f.write("print('{}')\n".format(Oid_list))
    f.write("print('{0:0.1f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    f.write("print('{1:0.1f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    f.write("print('{2:0.1f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    f.write("print('{3:0.1f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    
    f.close()
        
__GetSensor__()    