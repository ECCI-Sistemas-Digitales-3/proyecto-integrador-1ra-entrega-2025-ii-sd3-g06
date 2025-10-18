import time

class Pin:
    OUT = 0
    def __init__(self, pin, mode):
        self.pin = pin
    def value(self, val):
        print(f"Pin {self.pin} -> {'ON' if val else 'OFF'}")

valvula = Pin(14, Pin.OUT)

for i in range(3):
    valvula.value(1)
    time.sleep(0.5)
    valvula.value(0)
    time.sleep(2)

