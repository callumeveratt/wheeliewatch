from neopixel import NeoPixel
from machine import Pin
from logger import *
from ha import *
import colours
import time

def set_neopixel_onecolour(r,g,b):
    write_log(f'Setting neopixel to {r},{g},{b}')
    strip = NeoPixel(Pin(28), 8)
    for i in range(0,7):
        strip[i] = (r,g,b)
    strip.write()

def set_neopixel_twocolour(r1,g1,b1,r2,g2,b2):
    write_log(f'Setting neopixel to {r1},{g1},{b1} and {r2},{g2},{b2}')
    strip = NeoPixel(Pin(28), 8)
    for i in range(0,3):
        strip[i] = (r1,g1,b1)
    for i in range(4,7):
        strip[i] = (r2,g2,b2)
    strip.write()

def brown_bin(bin):
    if 'black' in bin:
        write_log('Calling black & brown function')
        set_neopixel_twocolour(colours.black_r, colours.black_g, colours.black_b, colours.brown_r, colours.brown_g, colours.brown_b)
    elif 'green' in bin:
        write_log('Calling green & brown function')
        set_neopixel_twocolour(colours.green_r, colours.green_g, colours.green_b, colours.brown_r, colours.brown_g, colours.brown_b)
    elif 'purple' in bin:
        write_log('Calling purple & brown function')
        set_neopixel_twocolour(colours.purple_r, colours.purple_g, colours.purple_b, colours.brown_r, colours.brown_g, colours.brown_b) 

def black_bin():
    set_neopixel_onecolour(colours.black_r, colours.black_g, colours.black_b)

def green_bin():
    set_neopixel_onecolour(colours.green_r, colours.green_g, colours.green_b)

def purple_bin():
    set_neopixel_onecolour(colours.purple_r, colours.purple_g, colours.purple_b)
    
def error_bin():
    while True:
        set_neopixel_onecolour(colours.error_r, colours.error_g, colours.error_b)
        time.sleep(1)
        set_neopixel_onecolour(0,0,0)
        time.sleep(1)

def turn_off():
    set_neopixel_onecolour(0,0,0)
    
def set_rgb_colour(bin):
    if 'brown' in bin:
        write_log('Calling brown function to determine colours')
        brown_bin(bin)
    elif bin == 'black':
        write_log('Calling black function')
        black_bin()
    elif bin == 'green':
        write_log('Calling green function')
        green_bin()
    elif bin == 'purple':
        write_log('Calling purple function')
        purple_bin()
    elif bin == 'error':
        write_log('Calling error function')
        error_bin()