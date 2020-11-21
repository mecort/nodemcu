import time

from machine import Pin

response_template = """HTTP/1.0 200 OK

%s
"""

pin = Pin(9, Pin.OUT)

def light_on():
     pin.value(1)
     body = "You turned a light on!"
     return response_template % body

def light_off():
     pin.value(0)
     body = "You turned a light off!"
     return response_template % body

handlers = {
    'time': time,
    'dummy': dummy,
    'light_on': light_on,
    'light_off': light_off,
}