# Script that polls "server" ESP8266 for received HTTP requests over serial connection
# On success runs the "getSchedule.py" script to update the bus location database
# Sends the result back to the server over serial connection, where it can be queried

import serial
import subprocess

server = serial.Serial('COM7', 115200, timeout=.1) # open server serial port

while True:
    data = server.readline() # data in form b'asdsfdgsdgf'

    # ignore empty strings (since polling)
    if data == b'':
        continue

    # check for our header of "/" (ASCII 47), otherwise ignore
    if data[0] != 47:
        continue
    
    data = data.decode('utf-8') # decode from serial (decode ASCII)
        
    # Example decoded string: "/7:1138 Bathurst St\r\n"

    substrings = data[1:-2].split(":") # discard first char, last 2 char, and split on ":"
    print(substrings) # debug print query

    # parse data string and get arrival/departure time of next bus
    output = subprocess.check_output(["python","getSchedule.py",substrings[0],substrings[1]])

    print(output.decode('utf-8')) # debug print result of "getSchedule.py" script

    server.write(output) # send result back to server
    