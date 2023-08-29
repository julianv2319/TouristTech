from machine import ADC, Pin
from time import sleep

class BUZZER():
     def __init__(self, pin_buzzer):
         self.buzzer = Pin(pin_buzzer, Pin.OUT)
         
     def set_buzzer(self):
        self.buzzer.on()
    
     def clear_buzzer(self):
        self.buzzer.off()
        
     def play_buzzer(self,times):
         for i in range(times):
             self.set_buzzer()
             sleep(0.5)
             self.clear_buzzer()
             sleep(0.5)
         
class RELAY():
    
    def __init__(self, list_relays):
        self.relays = [ Pin(numberpin, Pin.OUT) for numberpin in list_relays ]
    
    def set_relay(self, number):
        self.relays[number].on()
    
    def clear_relay(self, number):
        self.relays[number].off()
    
    def get_status_relay(self, number):
        self.relays[number].value()

class LDR():
    
    def __init__(self, pinldr):
        self.ldr = ADC( Pin(pinldr) )
        
    def get_ldr_Value(self):
        return self.ldr.read()
    
class PIR():
    
    def __init__(self, pinpir):
        self.pir = Pin( pinpir, Pin.IN)
    
    def get_pir_Value(self):
        return self.pir.value()