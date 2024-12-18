from machine import Pin, ADC
from time import sleep

moisture_sensor = ADC(27)
led = Pin(12, Pin.OUT)

file_name = 'log.txt'

def log_message(msg):
    with open(file_name, 'a+') as log_file:
        log_file.write(msg + '\n')
        log_file.flush()
        
        file_size = log_file.tell()
        if file_size > 1024 * 1024: # 1 MB
            log_file.close()
            with open('log.txt', 'w') as log_file:
                log_file.write("log cleared\n")
                
try:
    while True:
        moisture_level = moisture_sensor.read_u16()
        print(f"moisture level {moisture_level}")
        log_message(f"moisture level {moisture_level}")
        if moisture_level > 27000:
            led.value(1)
            log_message("soil is dry")           
        else:
            led.value(0)
        sleep(5)

except KeyboardInterrupt:
    pass

finally:
    led.value(0)




        
        
        
