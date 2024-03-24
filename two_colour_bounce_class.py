# two colour bounce class
import time

class TwoColourBounce:
    
    SPEED = 40 # fps
    RED = (255,0,0)
    GREEN = (0,255,0)
    OFF = (0,0,0)

    def __init__(self, led_strip, flag, num_leds=50):
        self.led_strip=led_strip
        self.num_leds=num_leds
        self.flag=flag
        
        for i in range(self.num_leds):
            self.led_strip.set_rgb(i,*TwoColourBounce.OFF)
            
        self.animate()
        
    def animate(self):
        
        while True:

            # out
             for i in range(self.num_leds):
                 self.led_strip.set_rgb(i,*TwoColourBounce.GREEN)
                 time.sleep(1.0/TwoColourBounce.SPEED)
                 self.led_strip.set_rgb(i,*TwoColourBounce.OFF)
                 
             for i in range(self.num_leds-1,0,-1):
                 self.led_strip.set_rgb(i,*TwoColourBounce.RED)
                 time.sleep(1.0/TwoColourBounce.SPEED)
                 self.led_strip.set_rgb(i,*TwoColourBounce.OFF)
                 
             if self.flag.get_run_flag()==False:
                 self.clear()
                 break

    def clear(self):
        
        for i in range(self.num_leds):
            self.led_strip.set_rgb(i, 0,0,0)
