import time
import board
import digitalio
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Default output MIDI channel:", midi.out_channel + 1)

# A BUTTON
button_pinA = board.GP6
buttonA = digitalio.DigitalInOut(button_pinA)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.UP
buttonA_pressed = False

# B BUTTON
button_pinB = board.GP2
buttonB = digitalio.DigitalInOut(button_pinB)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.UP
buttonB_pressed = False

# C BUTTON
button_pinC = board.GP0
buttonC = digitalio.DigitalInOut(button_pinC)
buttonC.direction = digitalio.Direction.INPUT
buttonC.pull = digitalio.Pull.UP
buttonC_pressed = False

# PREV BUTTON
button_pinPREV = board.GP5
buttonPREV = digitalio.DigitalInOut(button_pinPREV)
buttonPREV.direction = digitalio.Direction.INPUT
buttonPREV.pull = digitalio.Pull.UP
buttonPREV_pressed = False

# STOP BUTTON
button_pinSTOP = board.GP3
buttonSTOP = digitalio.DigitalInOut(button_pinSTOP)
buttonSTOP.direction = digitalio.Direction.INPUT
buttonSTOP.pull = digitalio.Pull.UP
buttonSTOP_pressed = False

# NEXT BUTTON
button_pinNEXT = board.GP1
buttonNEXT = digitalio.DigitalInOut(button_pinNEXT)
buttonNEXT.direction = digitalio.Direction.INPUT
buttonNEXT.pull = digitalio.Pull.UP
buttonNEXT_pressed = False

# GO BUTTON
button_pinGO = board.GP4
buttonGO = digitalio.DigitalInOut(button_pinGO)
buttonGO.direction = digitalio.Direction.INPUT
buttonGO.pull = digitalio.Pull.UP
buttonGO_pressed = False

while True:
    if not buttonA.value and not buttonA_pressed:
        midi.send(NoteOn(44, 120))
        print("A pressed")
        buttonA_pressed = True
    elif buttonA.value and buttonA_pressed:
        midi.send(NoteOff(44, 120))
        print("A released")
        buttonA_pressed = False
    
    if not buttonB.value and not buttonB_pressed:
        midi.send(NoteOn(45, 120))
        print("B pressed")
        buttonB_pressed = True
    elif buttonB.value and buttonB_pressed:
        midi.send(NoteOff(45, 120))
        print("B released")
        buttonB_pressed = False
    
    if not buttonC.value and not buttonC_pressed:
        midi.send(NoteOn(46, 120))
        print("C pressed")
        buttonC_pressed = True
    elif buttonC.value and buttonC_pressed:
        midi.send(NoteOff(46, 120))
        print("C released")
        buttonC_pressed = False

    if not buttonPREV.value and not buttonPREV_pressed:
        midi.send(NoteOn(47, 120))
        print("PREV pressed")
        buttonPREV_pressed = True
    elif buttonPREV.value and buttonPREV_pressed:
        midi.send(NoteOff(47, 120))
        print("PREV released")
        buttonPREV_pressed = False
        
    if not buttonSTOP.value and not buttonSTOP_pressed:
        midi.send(NoteOn(48, 120))
        print("STOP pressed")
        buttonSTOP_pressed = True
    elif buttonSTOP.value and buttonSTOP_pressed:
        midi.send(NoteOff(48, 120))
        print("STOP released")
        buttonSTOP_pressed = False

    if not buttonNEXT.value and not buttonNEXT_pressed:
        midi.send(NoteOn(49, 120))
        print("NEXT pressed")
        buttonNEXT_pressed = True
    elif buttonNEXT.value and buttonNEXT_pressed:
        midi.send(NoteOff(49, 120))
        print("NEXT released")
        buttonNEXT_pressed = False

    if not buttonGO.value and not buttonGO_pressed:
        midi.send(NoteOn(50, 120))
        print("GO pressed")
        buttonGO_pressed = True
    elif buttonGO.value and buttonGO_pressed:
        midi.send(NoteOff(50, 120))
        print("GO released")
        buttonGO_pressed = False
