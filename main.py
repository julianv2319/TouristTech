from machine import Pin, I2C
from time import sleep
from bme680 import *
from TuristProject import *
from ESP_Connection import *

list_relay_connection = [14,27,26,25,33,32]

RELAY1=0
RELAY2=1
RELAY3=2
RELAY4=3
RELAY5=4
RELAY6=5

MY_SSID  = getSSID()
MY_PASS  = getPASS()
MY_TOKEN = getToken()

time_to_send = 30

def run():
    
    global time_to_send
    global should_publish
    global message_received
    
    counter_sample = 0
    wifi = ESP_Connect(SSID=MY_SSID, PASS= MY_PASS)
    wifi.connect_ubidots(MY_TOKEN)
    
    i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=100000)
    bme = BME680_I2C(i2c=i2c)
    ldr_interior = LDR(pinldr=34)
    ldr_exterior = LDR(pinldr=35)
    pirA = PIR(pinpir=15)
    pirB = PIR(pinpir=2)
    relays = RELAY(list_relays =list_relay_connection )
    buzzer = BUZZER(pin_buzzer=12)
    
    buzzer.play_buzzer(2)
    data="prueba"
    wifi.start_subscribe_thread(data)

    
    while (True):
        
        """       
        ldr_int_val = ldr_interior.get_ldr_Value()
        ldr_ext_val = ldr_exterior.get_ldr_Value()
        
        pirA_val = pirA.get_pir_Value()
        pirB_val = pirB.get_pir_Value()"""
        
        temp = bme.temperature
        hum  = bme.humidity
        pres = bme.pressure
        gas  = bme.gas
        
        "wifi.start_subscribe_thread()"
        
        if counter_sample == time_to_send:
            
            wifi.publish_ubidots(typeVar="Temperature",value=temp,context="AulaSteam")
            wifi.publish_ubidots(typeVar="Humidity",value=hum,context="AulaSteam")
            wifi.publish_ubidots(typeVar="Pressure",value=pres,context="AulaSteam")
            wifi.publish_ubidots(typeVar="Gas",value=gas,context="AulaSteam")
            counter_sample = 0
             
        
        print("Temp: ",temp)
        print("Hum: ",hum)
        print("Pres: ",pres)
        print("Gas: ",gas)
        print("")
        """print("LDR INT: ",ldr_int_val)
        print("LDR EXT: ",ldr_ext_val)
        print("")
        print("PIR A: ",pirA_val)
        print("PIR B: ",pirB_val)"""
        print("")
        counter_sample += 1
        sleep(0.3)
    
if __name__=="__main__":
    run()
    