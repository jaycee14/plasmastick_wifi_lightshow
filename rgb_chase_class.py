# rgb chase class
import time

class RGBChase:
    
	DELAY = 0.1
	R=(255,0,0)
	G=(0,255,0)
	B=(0,0,255)

	def __init__(self, led_strip, flag, num_leds=50):
		self.led_strip=led_strip
		self.num_leds=num_leds
		self.flag=flag
		self.buffer =  [(0,0,0) for n in range(self.num_leds)]
        
        # prepare an RGB array
		for i in range(self.num_leds):
				
			if (i+1) % 3 ==0:
				self.buffer[i]=RGBChase.R
			elif (i+1) % 2 == 0:
				self.buffer[i]=RGBChase.G
			else:
				self.buffer[i]=RGBChase.B
				
			self.led_strip.set_rgb(i,*self.buffer[i])
					
		self.animate()
        
	def animate(self):
		offset=0
		while True:

			for i in range(self.num_leds):
           
				buffer_idx = (offset+i) % self.num_leds
				self.led_strip.set_rgb(i,*self.buffer[buffer_idx])
         
				time.sleep(RGBChase.DELAY)
				offset += 1
				if offset > self.num_leds:
					offset=0
                 
			if self.flag.get_run_flag()==False:
				self.clear()
				break

	def clear(self):
        
		for i in range(self.num_leds):
			self.led_strip.set_rgb(i, 0,0,0)

    
    
        