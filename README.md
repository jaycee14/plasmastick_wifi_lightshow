# plasmastick_wifi_lightshow
Using the Pimoroni Plasmastick to run a light show with a web interface to set the light pattern. Multicore RP Pico 2040 W programming.

## Background

My not-particularly-serious but fun running club has an annual Xmas tradition of running round central London wearing any kind of lights we can. There's also usually some tunes and a lot of mulled wine stops. It's a great event and you get a lot of positive feedback from those you run past.

Previously I used some EL lights but wanted to step it up using the [Pimoroni plasmastick kit](https://shop.pimoroni.com/products/wireless-plasma-kit?variant=40372594704467) which is a great device mixing a Raspberry Pi Pico W with a neopixel strip which runs MicroPython or CircuitPython.
Pimoroni have produced a great set of [starter scripts](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/plasma_stick) and I have used the code from some of their light patterns as they were festive and really effective.

![Running Club](./IMG_4017.JPG)

## Operation
I wanted to be able to change the pattern displayed on the LED strip without an extensive set of switches and settled on the idea of using a web server to act as the interface - I would then use my mobile to connect to the Pico (running in Access Point mode) via wifi and interact with web buttons to change the setting.

## Threading
Pretty soon I realised that the web server and light show code would block each other. However the Pico is dual core so we can have one core operate the webserver and the other run the light show. This meant learning about some multithread programming in MicroPython. This [site](https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/) was of great use in helping set up a multithread approach and also communicate between the threads - or how the webserver told the light show to stop and change to a new patter.

## In Practice
This is not the most polished code, I was up late the night before the run getting it to work (and then attaching the lights to a running top!). However, despite my worries of crashing and needing a reboot it operated flawlessly for around three hours despite several connections and pattern requests, the cold and being stuffed into a bumbag and being jogged round London.
The pattern classes could definitely benefit from a bit more inheritance and maybe some auto updating the webpage but it worked when it needed to. 





