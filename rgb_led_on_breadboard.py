# Created by: Jaeyoon Lee
# Created on: Dec 2021
#
#  Turn RGB LED on and rotate through each color:
#    red, green, blue, purple, cyan, magenta, yellow and white


import time
import board
import digitalio

led_red = digitalio.DigitalInOut(board.GP16)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.GP19)
led_green.direction = digitalio.Direction.OUTPUT
led_blue = digitalio.DigitalInOut(board.GP18)
led_blue.direction = digitalio.Direction.OUTPUT

def rgb_color(red, green, blue):
    led_red.value = red
    led_green.value = green
    led_blue.value = blue
    time.sleep(1)


while True:
    rgb_color(True, False, False)
    rgb_color(False, True, False)
    rgb_color(False, False, True)
    rgb_color(True, True, False)
    rgb_color(True, False, True)
    rgb_color(False, True, True)
    rgb_color(True, True, True)
