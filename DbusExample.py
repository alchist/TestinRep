def main():
	import dbus
	bus = dbus.SystemBus()
	eth0 = bus.get_object('org.freedesktop.NetworkManager','/org/freedesktop/NetworkManager/Devices/eth0')
	eth0_dev_iface = dbus.Interface(eth0,dbus_interface='org.freedesktop.NetworkManager.Devices')
	props = eth0_dev_iface.getProperties()
	print str(props)
if __name__ == '__main__':
  main()