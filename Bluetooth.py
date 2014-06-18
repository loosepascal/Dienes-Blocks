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
import time
print "performing inquiry.."

datalist = []
target_address = None
target_name = "jyl2"
port = 1
nearby_devices = bluetooth.discover_devices(lookup_names=True)

print "found %d devices" % len(nearby_devices)
for name, addr in nearby_devices:
    print " %s - %s" % (addr,name)

#bluetooth address of the bluetooth module is 00:12:02:28:73:47
##for bdaddr in nearby_devices:
##    if target_name == bluetooth.lookup_name( bdaddr ):
##        target_address = bdaddr
##        break
##
##if target_address is not None:
##    print "found target bluetooth device with address ", target_address


client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

##server_socket.bind(("", ))
##server_socket.listen(1)
##
##client_socket,address = server_socket.accept()
##print "Accepted connection from ",address

client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
print "connected to server"

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
                #client_socket.send("Q124")
                #time.sleep(5)
##                Thousands = datalist[0]
##                Hundreds = datalist[1]
##                Tens = datalist[2]
##                Units = datalist[3]

                              #have global variables that update with parsed bluetooth data

except KeyboardInterrupt:
     print "Closing socket...\n",
     client_socket.close()
     print "done."

##else:
##    print "could not find target bluetooth device nearby"

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