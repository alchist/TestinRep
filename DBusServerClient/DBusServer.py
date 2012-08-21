#!/usr/bin/env python
import gtk
import dbus, sys
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
class MyServer(dbus.service.Object):
    def __init__(self):
        bus_name=dbus.service.BusName('org.alchist.echoservice',bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/alchist/echoservice')
    text='another text' 
    @dbus.service.signal('org.alchist.echoservice')
    def echo_signal(self):
        print  'Signal work, echo change to', self.text
    @dbus.service.method('org.alchist.echoservice')
    def echo(self):
        return self.text
    @dbus.service.method('org.alchist.echoservice')
    def change_echo(self, new_echo):
        self.text=new_echo
        self.echo_signal()
        return 0
DBusGMainLoop(set_as_default=True)
myservice=MyServer()

gtk.main()

