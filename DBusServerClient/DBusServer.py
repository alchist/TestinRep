#!/usr/bin/env python
import gtk
import dbus, sys
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
class MyServer(dbus.service.Object):
    def __init__(self):
        bus_name=dbus.service.BusName('org.alchist.echoservice',bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/alchist/echoservice')

    @dbus.service.method('org.alchist.echoservice')
    def echo(self, variant):
        return str(variant)
DBusGMainLoop(set_as_default=True)
myservice=MyServer()
gtk.main()
