import usb_hid, usb_midi, usb_cdc
import supervisor
import storage
import board, digitalio

supervisor.set_usb_identification(manufacturer="Ex Machina", product="USB Go Box")
usb_hid.disable()
usb_midi.enable()
usb_midi.set_names(streaming_interface_name="Ex Machina USB Go Box", audio_control_interface_name="Ex Machina USB Go Box", in_jack_name="USB Go Box midi port", out_jack_name="USB Go Box midi port")

storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "usb_go_box"
storage.remount("/", readonly=True)
storage.enable_usb_drive()

button = digitalio.DigitalInOut(board.GP29)
button.pull = digitalio.Pull.DOWN

if not button.value:
#    storage.disable_usb_drive()
#    usb_cdc.disable()
