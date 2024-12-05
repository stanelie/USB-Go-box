import usb_hid, usb_midi
import supervisor
import storage

supervisor.set_usb_identification(manufacturer="Ex Machina", product="USB Go Box")
usb_hid.disable()
usb_midi.enable()
# usb_midi.set_names(streaming_interface_name="CircuitPython MIDI", audio_control_interface_name="CircuitPython Audio", in_jack_name="CircuitPython usb_midi.ports[0]", out_jack_name="CircuitPython usb_midi.ports[0]")
# usb_midi.set_names(streaming_interface_name="new_streaming_interface_name", audio_control_interface_name="new_control_interface_name", in_jack_name="new_in_jack_name", out_jack_name="new_out_jack_name")
# usb_midi.set_names(streaming_interface_name="new_streaming_interface_name", audio_control_interface_name="new_udio_control_interface_name", in_jack_name="new_in_jack_name", out_jack_name="new_out_jack_name")
usb_midi.set_names(audio_control_interface_name="Ex Machina USB Go Box")



storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "usb_go_box"
storage.remount("/", readonly=True)
storage.enable_usb_drive()
