#-------------------------------------------------------------------------------
# Name:        Bluetooth Test
# Purpose:
#
# Author:      Christos Karpis
#
# Created:     30/05/2014
# Copyright:   (c) Christos Karpis 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import bluetooth

print "performing inquiry.."

datalist = []
nearby_devices = bluetooth.discover_devices(lookup_names=True)

print "found %d devices" % len(nearby_devices)
for name, addr in nearby_devices:
    print " %s - %s" % (addr,name)

#bluetooth address of the bluetooth module is 00:12:02:28:73:47

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
print "connected to server"
##while x==0:
##    data = client_socket.recv(65536)
##    print "received [%s]" % data
##    if data != " ":
##         #have global variables that update with parsed bluetooth data

#data = ""
try:
     while True:
         try:
             data = client_socket.recv(65536)
         except bluetooth.BluetoothError, b:
             print "Bluetooth Error: ", b
         else:
            if data != " ":
                print "received [%s]" % data
                datalist = data.split(' ')
                print datalist
                Thousands = datalist[0]
                Hundreds = datalist[1]
                Tens = datalist[2]
                Units = datalist[3]

                              #have global variables that update with parsed bluetooth data

except KeyboardInterrupt:
     print "Closing socket...\n",
     client_socket.close()
     print "done."



##target_name = "Christos Karpis"
##target_address = None
##
##nearby_devices = bluetooth.discover_devices()
##
##for bdaddr in nearby_devices:
##    if target_name == bluetooth.lookup_name( bdaddr ):
##        target_address = bdaddr
##        break
##
##if target_address is not None:
##    print "found target bluetooth device with address ", target_address
##else:
##    print "could not find target bluetooth device nearby"