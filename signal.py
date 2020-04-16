#!/usr/bin/env python
import skywriter
import signal
import RPi.GPIO as GPIO
import time

channelleft = 21
channelright = 20
blinkleft = 12
blinkright = 16
GPIO.setmode(GPIO.BCM)
some_value = 5000
GPIO.setup(channelleft, GPIO.OUT)
GPIO.setup(channelright, GPIO.OUT)
GPIO.setup(blinkleft, GPIO.OUT)
GPIO.setup(blinkright, GPIO.OUT)

GPIO.output(16,1)
time.sleep(1)

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
