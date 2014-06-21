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
#search for bluetooth devices
#(---------multiple modules?--------------)
#make connection with module
#//START
#    send question to child
#   //wait for confirmation, start timeout1 to limit time for confimation to come back,
#  //if timeout1 >t1  and no confirmation, resend answer
#  # //if timeout1 >t2 without confirmation, display warning on adult's screen(Board not receiving
#//if conf received,
# start checking if answer arrived, start timeout2
#      //answer not received and timeout2>t - tell teacher child has not responded
#      //Answer received-> send conf
#//go to START

import bluetooth
import time
print "performing inquiry.."

confirmation_timeout = 2
resend_timeout = 5
answer_timeout = 300 #make very large to allow child to submit an answer
C = 0
A = 0
escape = 0

question = ["123", "250","473", "207","152","360","299", "101","564","658"]


Question_String = 'Q'
qcount = 0

target_address = None
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
             client_socket.send(question[qcount])
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

         except bluetooth.BluetoothError, b:
             print "Bluetooth Error: ", b
         else:
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
            qcount = qcount + 1
            if(qcount == 10):
                qcount = 0


except KeyboardInterrupt:
     print "Closing socket...\n",
     client_socket.close()
     print "done."


print "Closing socket...\n",
client_socket.close()
print "done."
