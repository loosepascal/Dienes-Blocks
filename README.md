## Connecting to Bluetooth

To connect to bluetooth you need to configure the serial port of the Arduino within Arduino IDE. Depending on your OS you need to install PySerial for OS X or Bluetooth for Windows. 

Whichever port you select, you need to adjust the Python code.
    ser = serial.Serial('/dev/cu.jyl2-DevB', 9600)
