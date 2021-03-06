#-------------------------------------------------------------------------------
# Name:        Bluetooth T->C
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

confirmation_timeout = 2
resend_timeout = 5
answer_timeout = 20 #make very large to allow child to submit an answer
C = 0
A = 0
escape = 0
reconnected = 0
question = 567
Question_String = 'Q'

target_address = "00:12:02:28:73:47"
target_name = "jyl2"
port = 1
nearby_devices = bluetooth.discover_devices(lookup_names=True)

print "found %d devices" % len(nearby_devices)
for name, addr in nearby_devices:
    print " %s - %s" % (addr,name)

#bluetooth address of the bluetooth module is 00:12:02:28:73:47
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
print "connected to server"

try:
     while True:
         try:
             client_socket.send("Q")
             client_socket.send(str(question))
             print str(question)
             print "question sent"
             #time.sleep(5)
             start = time.time()
             #print start
             while (C == 0) : #if there Is data OR we have not yet read any data from a Question packet #(len(client_socket.recv(65536)) > 0)  ||
                print "confirmation loop started"
                data  = client_socket.recv(1024) #waits until there is data to be received
                if len(data) != 0:
                    print "received [%s]" % data
                print "confirmation data printed\n"

                if(data == 'C') :
                    C = 1

                if(((time.time() - start) > confirmation_timeout) and (C == 0)):
                    client_socket.send("Q")
                    client_socket.send(str(question))
                    print "message re-sent"

                   #count number of resends (if not using timeout3)
                   #if timeout2 >t2/number of resends exceeded without confirmation, display warning on child's screen
                if(((time.time() - start) > resend_timeout) and (C == 0)):
                         #while(1):
                            print "!!!!!!!!!!!!!!!BOARD NOT RECEIVING! (resend_timeout) !!!!!!!!!!!!!!!!!" #/call function to display warning on screen and halt program
                            escape = 1
                            break
                time.sleep(1)
             if(escape == 1):
                escape = 0
                break

             print "Closing socket after receiving confirmation...\n"
             client_socket.close()
             print "done."


         except bluetooth.BluetoothError, b:
             print "Bluetooth Error: ", b
         else:
            time.sleep(10)
            while (reconnected == 0):
                start = time.time()
                nearby_devices2 = bluetooth.discover_devices( flush_cache=False, lookup_names=False  )  #discoverdevcies() scans for about 10 seconds
                #if lookup_names is False, returns a list of bluetooth addresses.
                #if lookup_names is True, returns a list of (address, name) tuples
                print "found %d devices" % len(nearby_devices2)
                #for name, addr in nearby_devices2:
                 #   print " %s - %s" % (addr,name)
                for address in nearby_devices2:
                    if target_address == address:#target_name == bluetooth.lookup_name(address):
                        print "found jyl2"
                        reconnected = 1


                        client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                        client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
                        print "reconnected to server"

            print (time.time() - start)
            start = time.time()

            while (A == 0):
                answer_confirmation  = client_socket.recv(1024) # note that the A character is received separately from the answer and requires 2 recv.() calls
                print "answer_confirmation [%s]"% (answer_confirmation)
                if(answer_confirmation == 'A'):
                    answer_data = client_socket.recv(1024)
                    print "answer_data [%s]" % answer_data

                    A = 1
                if((time.time() - start)> answer_timeout):
                        print "!!!!!!!!!!!!!!!NOT RECEIVING ANSWER! (answer_timeout) !!!!!!!!!!!!!!!!!" #/call function to display warning on screen and halt program
                        escape = 1
                        break
            if(escape == 1):
                escape = 0
                break

            client_socket.send("C")
            time.sleep(1)
            C=0
            A=0
            reconnected = 0


except KeyboardInterrupt:
     print "Closing socket...\n",
     client_socket.close()
     print "done."


print "Closing socket...\n",
client_socket.close()
print "done."