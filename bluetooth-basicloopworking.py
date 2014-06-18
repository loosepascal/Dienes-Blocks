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
answer_timeout = 5 #make very large to allow child to submit an answer
C = 0
A = 0
escape = 0


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


try:
     while True:
         try:
             client_socket.send("Q0234")
             print "question sent"
##             client_socket.send("1")
##             client_socket.send("2")
##             client_socket.send("3")
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
                    client_socket.send("Q0234")
                    print "message re-sent"

                   #count number of resends (if not using timeout3)
                   #if timeout2 >t2/number of resends exceeded without confirmation, display warning on child's screen
                if(((time.time() - start) > resend_timeout) and (C == 0)):
                         #while(1):
                            print "!!!!!!!!!!!!!!!BOARD NOT RECEIVING! (resend_timeout) !!!!!!!!!!!!!!!!!" #/call function to display warning on screen and halt program
                            escape = 1
                            break
##                            print "\nClosing socket...\n",
##                            client_socket.close()
##                            print "done."
                time.sleep(1)
             if(escape == 1):
                escape = 0
                break

         except bluetooth.BluetoothError, b:
             print "Bluetooth Error: ", b
         else:
            start = time.time()

            while (A == 0):
                answer_confirmation  = client_socket.recv(1024)
                print answer_confirmation


                #datalist = answer_data.split(',')
                #print datalist
                if(datalist[0] == 'A'):
                    answer_data = client_socket.recv(1024)
                    print "answer  data = "
                    print answer_data
                    A = 1
                if((time.time() - start)> answer_timeout):
                    #while(1):
                        print "!!!!!!!!!!!!!!!NOT RECEIVING ANSWER! (answer_timeout) !!!!!!!!!!!!!!!!!" #/call function to display warning on screen and halt program
                        escape = 1
                        break
            if(escape == 1):
                escape = 0
                break

##            for num in range(0, 4):#0 to 3
##                data = client_socket.recv(65536)
##                datalist.append(data)
##            print datalist
            print "%d" % len(datalist)
            start = time.time()
            #while((time.time() - start) < 1):
            client_socket.send("C")
            #print time.time()
            time.sleep(1)
            C=0
            A=0
            datalist = []
##            print "happy"




except KeyboardInterrupt:
     print "Closing socket...\n",
     client_socket.close()
     print "done."


print "Closing socket...\n",
client_socket.close()
print "done."
#read data (4 reads) and send confirmation


##                datalist = data.split(' ')
##                print datalist
##
##                time.sleep(5)
##                  data = client_socket.recv(65536)
##                Thousands = datalist[0]
##                Hundreds = datalist[1]
##                Tens = datalist[2]
##                Units = datalist[3]

                              #have global variables that update with parsed bluetooth data


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