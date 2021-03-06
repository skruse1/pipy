#!/usr/bin/env python
import skywriter
import signal
import RPi.GPIO as GPIO
import time

channelleft = 21
channelright = 20

GPIO.setmode(GPIO.BCM)
some_value = 5000
GPIO.setup(channelleft, GPIO.OUT)
GPIO.setup(channelright, GPIO.OUT)
GPIO.setup(channelright, GPIO.IN)
GPIO.setup(channelleft, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
state1 = GPIO.input(channelright)
state2 = GPIO.input(channelleft)


def blinkleft():
        GPIO.output(16,1)## Switch on pin 11
        time.sleep(1)## Wait
        GPIO.output(16,0)## Switch off pin 11
        time.sleep(1)## Wait
        state2 = GPIO.input(channelleft)

def blinkright():
        GPIO.output(12,1)## Switch on pin 11
        time.sleep(1)## Wait
        GPIO.output(12,0)## Switch off pin 11
        time.sleep(1)## Wait
        state1 = GPIO.input(channelright)
        
while state1 == 1:
        blinkright()
        GPIO.output(12, 1)
        if state1 == 0:
            break        
        
while state2 == 1:
        blinkleft()
        GPIO.output(16, 1)
        if state2 == 0:
            break     


#@skywriter.move()
#def move(x, y, z):
#  print( x, y, z )
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
   
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


@skywriter.flick()
def flick(start,finish):
  if start == 'east':
      print('Turn Left')
      motor_on(channelleft)
  elif start == 'west':
      print('Turn Right')
      motor_on(channelright)
  elif start == 'south':
      print('Off')
      motor_off(channelleft)
      motor_off(channelright)
  elif start == 'north':
      print('Off')
      motor_off(channelleft)
      motor_off(channelright)
     
@skywriter.airwheel()
def spinny(delta):
  global some_value
  some_value += delta
 
 
  if some_value > 10000:
    some_value = 10000
  print('Off')
  motor_off(channelleft)
  motor_off(channelright)


@skywriter.double_tap()
def doubletap(position):
  print('Off', position)
  motor_off(channelleft)
  motor_off(channelright)
 
@skywriter.tap()
def tap(position):
  print('Off', position)
  motor_off(channelleft)
  motor_off(channelright)
 
@skywriter.touch()
def touch(position):
  print('Off', position)
  motor_off(channelleft)
  motor_off(channelright)
 
signal.pause()
