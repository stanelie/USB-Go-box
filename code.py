import time
import board
import digitalio
import usb_midi
import adafruit_midi
import neopixel
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# --- CONFIGURATION ---
DEBOUNCE_TIME = 0.05  # 50ms lockout
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, pixel_order=neopixel.RGB)
pixel.brightness = 0.5
pixel.fill((5, 0, 0)) 

BUTTON_CONFIGS = [
    (board.GP6, 44, (0, 0, 255), "A"),
    (board.GP2, 45, (0, 0, 255), "B"),
    (board.GP0, 46, (0, 0, 255), "C"),
    (board.GP5, 47, (255, 100, 0), "PREV"),
    (board.GP3, 48, (255, 0, 0), "STOP"),
    (board.GP1, 49, (255, 100, 0), "NEXT"),
    (board.GP4, 50, (0, 255, 0), "GO"),
]

buttons = []
for pin, note, color, name in BUTTON_CONFIGS:
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    buttons.append({
        "io": io,
        "note": note,
        "color": color,
        "name": name,
        "active_pressed": False, 
        "last_press_time": 0      
    })

print("MIDI Go Box Initialized - LED Hold Enabled")

while True:
    current_time = time.monotonic()
    
    # We'll use this to decide if the pixel should be cleared
    any_button_active = False

    for btn in buttons:
        is_physically_pressed = not btn["io"].value
        time_since_press = current_time - btn["last_press_time"]

        # --- PRESS LOGIC ---
        if is_physically_pressed and not btn["active_pressed"]:
            if time_since_press > DEBOUNCE_TIME:
                midi.send(NoteOn(btn["note"], 120))
                btn["active_pressed"] = True
                btn["last_press_time"] = current_time
                pixel.fill(btn["color"])
                print(f"MIDI Send: {btn['name']}")

        # --- RELEASE LOGIC ---
        elif not is_physically_pressed and btn["active_pressed"]:
            midi.send(NoteOff(btn["note"], 120))
            btn["active_pressed"] = False
            print(f"MIDI Release: {btn['name']}")

        # --- LED PERSISTENCE LOGIC ---
        # If a button was recently pressed (within debounce window) 
        # or is still being held down, we keep the "active" flag up.
        if btn["active_pressed"] or (time_since_press < DEBOUNCE_TIME):
            any_button_active = True

    # If no buttons are held AND the debounce window has passed for all...
    if not any_button_active:
        # Reset to dim red (idle state)
        if pixel[0] != (5, 0, 0):
            pixel.fill((0, 0, 0)) # Or (5,0,0) if you want the idle glow
