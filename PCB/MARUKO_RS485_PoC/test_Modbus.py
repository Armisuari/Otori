#!/usr/bin/env python3
import ASUS.GPIO as GPIO
from multiprocessing import connection
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


client = ModbusClient(method='rtu', port='/dev/ttyS1', stopbits=1, bytesize=8, parity='N', baudrate=9600, timeout=0.3, strict=False)
connection = client.connect()

print(connection)

#GPIO.output(40, GPIO.LOW)
#value = client.read_input_registers(3, 2, unit=0x04)
#GPIO.output(40, GPIO.LOW)
value = client.read_holding_registers(0, 3, unit=0x06)
#print(value.registers)

if not value.isError():
    '''isError() method implemented in pymodbus 1.4.0 and later'''
    print(value.registers)

else:
    # Do stuff to error handling.
    print('Error message: {}'.format(value))