import sys
from machine import Pin, PWM
import utime
sys.path.insert(0, '../sound/')
from sound import tones
buzzer = PWM(Pin(16))
button = Pin(17, Pin.IN, Pin.PULL_DOWN)
led = Pin(18, Pin.OUT)

# debounce TIME saying 500ms between button presses
DEBOUNCE_UTIME = 500
# debounce counter is our counter from the last button press
# initialize to current time
debounce_counter = utime.ticks_ms()

led.value(0) # init led to off
# Flag for if LED is on or off
led_on = False

# song of time
song = ["A5","D4","P","F4","A5","D4","P","F4","A5","C5","B5","G4","F4","G4","A5","D4","C4","E4","D4"]
steps = [1,1,1,1,1,1,1,1,.5,.5,1, 1,.5,.5,1,1,.5,.5,2]

#Yum, Yum, Vegetables
#song = ["C4","P","D4","P","C4","D4","P","E4","P","F4","P","G4"]
#steps = [1.5,.5,1.5,.5,.75,.5,.025,.5,.025,.5,.025,.5]


def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            led_off()
            bequiet()
        else:
            led_on()
            playtone(tones.tones[mysong[i]])
        utime.sleep(0.6 * steps[i])
        led_off()
    led_off()
    bequiet()

# Function to handle when the button is pressed
def button_press_detected():
    global debounce_counter
    current_utime = utime.ticks_ms()
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)
    print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_UTIME):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()
        playsong(song)
    
    else:
        print("Not enough utime")
        
def led_off():
    led.value(0)
    led_on = False

def led_on():
    led.value(1)
    led_on = True

def toggle_led():
    global led_on
    if(led_on):
        led_off()
    else:
        led_on()

while True:
    if button.value()==True:
        button_press_detected()