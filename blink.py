import RPi.GPIO as gpio
import time

# Seteando el modo BOARD, la numeración de las salidas es la de la placa
pin_led = 13
gpio.setmode(gpio.BOARD)

# Seteando el modo BCM, la numeración de las salidas es la de GPIO
# pin_led = 27
# gpio.setmode(gpio.BCM)


gpio.setup(pin_led,gpio.OUT)

while(1):
    gpio.output(pin_led,True)
    time.sleep(0.5)

    gpio.output(pin_led,False)
    time.sleep(0.5)

