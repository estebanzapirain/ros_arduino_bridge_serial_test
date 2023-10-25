# Comunicación serie entre Python y Arduino ROS Bridge
# Repositorio del sketch arduino:
# https://github.com/joshnewans/ros_arduino_bridge
# Este script envía un comando 'a 0' al Arduino indicando que desea realizar una lectura analógica del puerto A0 e imprime la respuesta

#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    arduino = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
    arduino.reset_input_buffer()
    while True:
        # ser.write(b"b")
        arduino.write(b'a 0\r\n')
        valor = arduino.readline().decode('ascii').rstrip()
        if valor != b'':
                print(valor)
        time.sleep(0.01)
