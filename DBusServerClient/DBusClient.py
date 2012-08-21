#!/usr/bin/env python
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject

def echo_change_callback():
	print "echo message is changed"

DBusGMainLoop(set_as_default=True)
loop=gobject.MainLoop()
bus=dbus.SessionBus()
bus.add_signal_receiver(echo_change_callback,'echo_signal')
echo_service=bus.get_object('org.alchist.echoservice','/org/alchist/echoservice')
echo_string=echo_service.echo()
print echo_string
echo_service.change_echo('new text')
echo_string=echo_service.echo()
print echo_string
loop.run()