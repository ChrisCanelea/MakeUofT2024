# Skeleton code for receiving Serial input
import serial
import time
import subprocess

server = serial.Serial('COM7', 115200, timeout=.1)

# time.sleep(2)

while True:
    data = server.readline()
    # data in form b'asdsfdgsdgf'

    # skip empty strings
    if data == b'':
        continue

    # check for our header
    if data[0] != 47:
        continue
    
    # decode from serial (decode ascii)
    data = data.decode('utf-8')

    if data[0] == "/": # got key
        
        # "/7:1138 Bathurst St\r\n"

        substrings = data[1:-2].split(":")
        print(substrings)

        # parse data string and get arrival/departure time of next bus
        output = subprocess.check_output(["python","getSchedule.py",substrings[0],substrings[1]])

        # debug print
        print(output.decode('utf-8'))

        server.write(output) # send result back to server
    