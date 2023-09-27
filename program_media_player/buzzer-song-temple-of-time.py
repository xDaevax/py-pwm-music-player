import sys
from machine import Pin, PWM
from utime import sleep
sys.path.insert(0, '../sound/')
from sound import tones
buzzer = PWM(Pin(9))


song = ["A5","D4","P","F4","A5","D4","P","F4","A5","C5","B5","G4","F4","G4","A5","D4","C4","E4","D4"]
steps = [1,1,1,1,1,1,1,1,.5,.5,1, 1,.5,.5,1,1,.5,.5,2]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        sleep(0.6 * steps[i])
    bequiet()
playsong(song)