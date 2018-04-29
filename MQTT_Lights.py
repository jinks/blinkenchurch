#!/usr/bin/env python3

#imports
import smbus
import time
import socket
import paho.mqtt.client as paho

#variables
bus       = smbus.SMBus(1) # use 1 for Rev 2 Pi, Use 0 for Rev 1 Pi
swirlTime = 0.1            # how quick the swirl patern runs
blinkTime = 0.2            # how fast the lights blink
broker    = "127.0.0.1"    # address of MQTT Broker

# Device Addresses
devices = [ 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, ]
# Use only one device for testing, comment out to use all
devices = [ 0x20 ]

# Registers A are for GPA pins, Registers B are for GPB pins
IODIRA = 0x00 # Register A for pin direction
IODIRB = 0x01 # Register B for pin direction
OLATA  = 0x14 # Register A for outputs
OLATB  = 0x15 # Register B for outputs

#functions
def setup(device):
    print(f"Setting up device #0x{device}")
    # Set GPA and GPB pins to outputs
    bus.write_byte_data(device,IODIRA,0x00)
    bus.write_byte_data(device,IODIRB,0x00)
    # Set all outputs to off
    bus.write_byte_data(device,OLATA,0x00)
    bus.write_byte_data(device,OLATB,0x00)

#light animations
def clear(addr):
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)

def errorState():
    purpleBlink(devices[0])

def idleState(addr):
    bus.write_byte_data(addr,OLATB,0x80)

#Blinks
def redBlink(addr):
    bus.write_byte_data(addr,OLATA,0x49)
    bus.write_byte_data(addr,OLATB,0x12)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def blueBlink(addr):
    bus.write_byte_data(addr,OLATA,0x92)
    bus.write_byte_data(addr,OLATB,0x24)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def purpleBlink(addr):
    bus.write_byte_data(addr,OLATA,0xDB)
    bus.write_byte_data(addr,OLATB,0x36)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def greenBlink(addr):
    bus.write_byte_data(addr,OLATA,0x24)
    bus.write_byte_data(addr,OLATB,0x49)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def yellowBlink(addr):
    bus.write_byte_data(addr,OLATA,0x6D)
    bus.write_byte_data(addr,OLATB,0x5B)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def lightBlueBlink(addr):
    bus.write_byte_data(addr,OLATA,0xB6)
    bus.write_byte_data(addr,OLATB,0x6D)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

def whiteBlink(addr):
    bus.write_byte_data(addr,OLATA,0xFF)
    bus.write_byte_data(addr,OLATB,0x7F)
    time.sleep(blinkTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(blinkTime)

#Swirls
def redSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x01)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x08)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x40)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x02)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x10)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def blueSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x02)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x10)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x80)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x04)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x20)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def greenSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x04)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x20)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x01)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x08)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x40)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def purpleSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x03)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x18)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0xc0)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x06)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x30)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def yellowSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x05)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x28)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x40)
    bus.write_byte_data(addr,OLATB,0x01)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x0A)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x50)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def lightBlueSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x06)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x30)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x80)
    bus.write_byte_data(addr,OLATB,0x01)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x0C)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x60)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

def whiteSwirl(addr):
    bus.write_byte_data(addr,OLATA,0x07)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x38)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0xC0)
    bus.write_byte_data(addr,OLATB,0x01)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATA,0x00)
    bus.write_byte_data(addr,OLATB,0x0E)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x70)
    time.sleep(swirlTime)
    bus.write_byte_data(addr,OLATB,0x00)
    time.sleep(swirlTime)

#MQTT callback and monitoring
def on_message(client, usrdata, message):
    msg = str(message.payload.decode("utf-8")).strip()
    print("received message =",msg)
    #commands section
    if msg == "clear":
        clear(devices[0])
    elif msg == "idle":
        idleState(devices[0])
    elif msg == "close":
        redBlink(devices[0])
        print("Closing Connection")
        client.disconnect()
        client.loop_stop()
        print("Program Shutdown")
    else:
        errorState()

def main():
    for dev in devices:
        setup(dev)
    client = paho.Client("client-001") #create client object
    client.on_message=on_message #Bind function to callback

    print("connecting to broker ",broker)
    client.connect(broker)
    print("Subscribing")
    client.subscribe("lights")
    client.loop_forever() #start loop to process recieved messages

if __name__ == "__main__":
    main()
