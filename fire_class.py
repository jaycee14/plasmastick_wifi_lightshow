# fire class
import time
from random import random, uniform

class Fire:

    def __init__(self, led_strip, flag, num_leds=50):
        self.led_strip=led_strip
        self.num_leds=num_leds
        self.flag=flag
            
        self.animate()
        
    def animate(self):

		while True:
			# fire effect! Random red/orange hue, full saturation, random brightness
			for i in range(self.num_leds):
				self.led_strip.set_hsv(i, uniform(0.0, 50 / 360), 1.0, random())
				time.sleep(0.1)
						 
			if self.flag.get_run_flag()==False:
				self.clear()
				break

    def clear(self):
        
        for i in range(self.num_leds):
            self.led_strip.set_rgb(i, 0,0,0)

