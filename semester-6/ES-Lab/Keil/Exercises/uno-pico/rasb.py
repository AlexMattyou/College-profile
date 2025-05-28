from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    if uart.any():
        print(uart.read().decode('utf-8'))
    uart.write('H')
    time.sleep(2)
