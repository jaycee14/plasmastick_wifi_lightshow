# two colour bounce class
import time

class CentralEmit:

	SPEED = 40 # fps
	RED = (255,0,0)
	OFF = (0,0,0)

	def __init__(self, led_strip, flag, num_leds=50):
		self.led_strip=led_strip
		self.num_leds=num_leds
		self.flag=flag
		
		self.MID = self.num_leds//2
		
		for i in range(self.num_leds):
			self.led_strip.set_rgb(i,*CentralEmit.OFF)
			
		self.animate()
		
	def animate(self):
		while True:
			for i in range(self.MID,0,-1): #MID -0
			
				self.led_strip.set_rgb(i,*CentralEmit.RED)
				self.led_strip.set_rgb(self.MID + (self.MID-i),*CentralEmit.RED)
				
				time.sleep(1.0/CentralEmit.SPEED)
				
				self.led_strip.set_rgb(i,*CentralEmit.OFF)
				self.led_strip.set_rgb(self.MID + (self.MID-i),*CentralEmit.OFF)
                 
			if self.flag.get_run_flag()==False:
				self.clear()
				break

	def clear(self):
        
		for i in range(self.num_leds):
			self.led_strip.set_rgb(i, 0,0,0)

