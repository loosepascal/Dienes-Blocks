from Tkinter import *
import time
import bluetooth

def main():
    global Thousands_data, Hundreds_data, Tens_data, Units_data
    print "performing inquiry.."

    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    print "found %d devices" % len(nearby_devices)
    for name, addr in nearby_devices:
        print " %s - %s" % (addr,name)

    #bluetooth address of the bluetooth module is 00:12:02:28:73:47

    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
    print "connected to server"

    root = Tk()

    Thousands = StringVar()
    Hundreds = StringVar()
    Tens = StringVar()
    Units = StringVar()

    thousands = Label( root, textvariable=Thousands, relief=RAISED )
    hundreds = Label( root, textvariable= Hundreds, relief=RAISED )
    tens = Label( root, textvariable=Tens, relief=RAISED )
    units = Label( root, textvariable=Units, relief=RAISED )

##    bluetooth_connect()

    ##Thousands_shit = 1
   # while True:
        #data_collect()
    datalist = []
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
                Thousands_data = datalist[0]
                Hundreds_data = datalist[1]
                Tens_data = datalist[2]
                Units_data = datalist[3]
    except:
        pass


    Thousands.set(Thousands_data)
##        Thousands_shit += 1
    Hundreds.set("Hundreds_shit")
    Tens.set("Tens_shit")
    Units.set("Units_shit")

    thousands.pack()
    hundreds.pack()
    tens.pack()
    units.pack()

    root.update_idletasks()
    time.sleep(1)

    root.mainloop()

def bluetooth_connect():
    print "performing inquiry.."

    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    print "found %d devices" % len(nearby_devices)
    for name, addr in nearby_devices:
        print " %s - %s" % (addr,name)

    #bluetooth address of the bluetooth module is 00:12:02:28:73:47

    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
    print "connected to server"


def data_collect():

    datalist = []
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
                Thousands_data = datalist[0]
                Hundreds_data = datalist[1]
                Tens_data = datalist[2]
                Units_data = datalist[3]
    except:
        pass


if __name__ == '__main__':
    main()
##                datalist = data.split(' ')
##                print datalist
##                Thousands_data = datalist[0]
##                Hundreds_data = datalist[1]
##                Tens_data = datalist[2]
##                Units_data = datalist[3]
##                Thousands.set(Thousands_data)
##                Hundreds.set(Hundreds_data)
##                Tens.set(Tens_data)
##                Units.set(Units_data)
##                thousands.pack()
##                hundreds.pack()
##                tens.pack()
##                units.pack()
##                root.update_idletasks()
##                time.sleep(1)
##                root.mainloop
##    except:
##        pass
##
##    Thousands.set(Thousands_data)
####        Thousands_shit += 1
##    Hundreds.set("Hundreds_shit")
##    Tens.set("Tens_shit")
##    Units.set("Units_shit")
##
##    thousands.pack()
##    hundreds.pack()
##    tens.pack()
##    units.pack()
##
##    root.update_idletasks()
##    time.sleep(1)
##
##    root.mainloop()

def bluetooth_connect():
    print "performing inquiry.."

    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    print "found %d devices" % len(nearby_devices)
    for name, addr in nearby_devices:
        print " %s - %s" % (addr,name)

    #bluetooth address of the bluetooth module is 00:12:02:28:73:47

    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect(("00:12:02:28:73:47", 1)) #client connects to the server on port 1
    print "connected to server"


def data_collect():

    datalist = []
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
                Thousands_data = datalist[0]
                Hundreds_data = datalist[1]
                Tens_data = datalist[2]
                Units_data = datalist[3]
    except:
        pass


if __name__ == '__main__':
    main()
