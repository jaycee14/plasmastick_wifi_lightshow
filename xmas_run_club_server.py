
import plasma
from plasma import plasma_stick
import network
import socket
from time import sleep
import _thread

from xmas_tree_class import XmasTree
from two_colour_bounce_class import TwoColourBounce
from rgb_chase_class import RGBChase
from fire_class import Fire
from central_emit_class import CentralEmit

# from machine import Pin
# from math import sin

#access point wifi details
ssid = 'pico'
password = 'pico1234'

station = network.WLAN(network.AP_IF)
station.config(essid=ssid, password=password)
station.active(True)

DEBUG=True


while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(50, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# start updating the LED strip
led_strip.start()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

class Flag:
    run_core_1 = True
 
    @classmethod
    def set_run_flag(cls):
        cls.run_core_1 = True
 
    @classmethod
    def clear_run_flag(cls):
        cls.run_core_1 = False
 
    @classmethod
    def get_run_flag(cls):
        return cls.run_core_1
    
def web_server():
    
	while True:
		conn, addr = s.accept()
		print('Got a connection from %s' % str(addr))
		request = conn.recv(1024)
		request = str(request)
		print('Content = %s' % request)
  
  # parse request for button
		show_loc = request.find('/?show=')
		print(show_loc)
		
		if show_loc>1:
			
			show = request[show_loc:show_loc+10]
			print(f'show:{show}')
			print(f'show:{show[-3:]}')
		
			if show[-3:] == 'xmt':
				  
				Flag.clear_run_flag()
				sleep(6)
				Flag.set_run_flag()
				second_thread = _thread.start_new_thread(run_lights_class, (XmasTree,led_strip,Flag))
			  
			elif show[-3:] =='tcb':
				  
				Flag.clear_run_flag()
				sleep(6)
				Flag.set_run_flag()
				second_thread = _thread.start_new_thread(run_lights_class, (TwoColourBounce,led_strip,Flag))
				
			elif show[-3:] =='fre':
				  
				Flag.clear_run_flag()
				sleep(6)
				Flag.set_run_flag()
				second_thread = _thread.start_new_thread(run_lights_class, (Fire,led_strip,Flag))
				
			elif show[-3:] =='rgb':
				  
				Flag.clear_run_flag()
				sleep(6)
				Flag.set_run_flag()
				second_thread = _thread.start_new_thread(run_lights_class, (RGBChase,led_strip,Flag))
				
			elif show[-3:] =='cem':
				  
				Flag.clear_run_flag()
				sleep(6)
				Flag.set_run_flag()
				second_thread = _thread.start_new_thread(run_lights_class, (CentralEmit,led_strip,Flag))
					
					
			elif show[-3:]=='off':
				if DEBUG:
					print(show)
					
				Flag.clear_run_flag()
			

		response = web_page()
		conn.send('HTTP/1.1 200 OK\n')
		conn.send('Content-Type: text/html\n')
		conn.send('Connection: close\n\n')
		conn.sendall(response)
		conn.close()



def web_page():
  
  html = """<html><head>
    <title>ESP Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" href="data:,">
      <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
      h1{color: #0F3376; padding: 2vh;}
      p{font-size: 1.5rem;}
      
      .button{display: inline-block;
          background-color: #e7bd3b; border: none; 
          border-radius: 4px;
          color: white;
          padding: 16px 40px;
          text-decoration: none;
          font-size: 30px;
          margin: 2px;
          cursor: pointer;}
  
      .button2{background-color: #4286f4;}
  </style>
  </head>
  <body>
  <h1>Run Club Lights Web Server</h1> 
  <p><a href="/?show=xmt"><button class="button">Xmas Tree</button></a></p>
  <p><a href="/?show=tcb"><button class="button">Two Colour Bounce</button></a></p>
  <p><a href="/?show=fre"><button class="button">Fire</button></a></p>
  <p><a href="/?show=rgb"><button class="button">RGB Chase</button></a></p>
  <p><a href="/?show=cem"><button class="button">Central Emit</button></a></p>
  <p><a href="/?show=off"><button class="button button2">OFF</button></a></p>
  
  </body>
  </html>"""
  
  return html
   
def run_lights_class(class_type, led_strip,flag_link):
    
    class_instance = class_type(led_strip,flag_link)


if __name__ == "__main__":
    
    second_thread = _thread.start_new_thread(run_lights_class, (XmasTree, led_strip,Flag))
    
    web_server()



