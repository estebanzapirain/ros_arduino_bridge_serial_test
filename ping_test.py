# Comunicación serie entre Python y Arduino ROS Bridge
# Repositorio del sketch arduino:
# https://github.com/joshnewans/ros_arduino_bridge

#!/usr/bin/env python3

import serial
import time

if __name__ == '__main__':
    arduino = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
    arduino.reset_input_buffer()
    while True:
        arduino.write(b'p 6\r\n')
        valor = arduino.readline().decode('ascii').rstrip()
        if valor != b'':
                print(valor)
        time.sleep(0.3)
