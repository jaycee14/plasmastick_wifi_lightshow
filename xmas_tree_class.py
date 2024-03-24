from random import random, choice
import time

class XmasTree:
    
    TREE_COLOUR = [0.34, 1.0, 0.6]
    LIGHT_RATIO = 8  # every nth pixel is a light, the rest are tree.
    LIGHT_COLOURS = ((0.0, 1.0, 1.0),   # red
                 (0.1, 1.0, 1.0),   # orange
                 (0.6, 1.0, 1.0),   # blue
                 (0.85, 0.4, 1.0))  # pink
    LIGHT_CHANGE_CHANCE = 0.5  # change to 0.0 if you want static lights


    def __init__(self, led_strip, flag, num_leds=50):
        # initial setup
        self.led_strip=led_strip
        self.num_leds=num_leds
        self.flag=flag
        
        for i in range(self.num_leds):
            if i % XmasTree.LIGHT_RATIO == 0:  # add an appropriate number of lights
                self.led_strip.set_hsv(i, *choice(XmasTree.LIGHT_COLOURS))  # choice randomly chooses from a list
            else:  # GREEN
                self.led_strip.set_hsv(i, *XmasTree.TREE_COLOUR)
                
        self.animate()

    def animate(self):

        # animate
        while True:
            for i in range(self.num_leds):
                if (i % XmasTree.LIGHT_RATIO == 0) and (random() < XmasTree.LIGHT_CHANGE_CHANCE):
                    self.led_strip.set_hsv(i, *choice(XmasTree.LIGHT_COLOURS))
            time.sleep(0.5)
            
            if self.flag.get_run_flag()==False:
                self.clear()
                break

    def clear(self):
        
        for i in range(self.num_leds):
            self.led_strip.set_rgb(i, 0,0,0)
            
    
