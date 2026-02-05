#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["RPi.GPIO"]
# ///
 
import RPi.GPIO as GPIO
import time
 
# Mode BCM
GPIO.setmode(GPIO.BCM)
 
# GPIOs
R = 17
G = 22
B = 18
 
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
 
def set_color(r, g, b):
    GPIO.output(R, r)
    GPIO.output(G, g)
    GPIO.output(B, b)
 
try:
    # Rouge
    set_color(1, 0, 0)
    time.sleep(2)
 
    # Vert
    set_color(0, 1, 0)
    time.sleep(2)
 
    # Bleu
    set_color(0, 0, 1)
    time.sleep(2)
 
    # Blanc
    set_color(1, 1, 1)
    time.sleep(2)
 
finally:
    GPIO.cleanup()