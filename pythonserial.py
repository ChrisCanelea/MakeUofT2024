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
        
        # "/45:111 Disco Rd\r\n"

        substrings = data[1:-2].split(":")
        print(substrings)

        # parse data string and get arrival/departure time of next bus
        subprocess.run(["python3","./GetFileFromAPI/getSchedule.py",substrings[0],substrings[1]])

        server.write(b'Success') # send result back to server
    
    print(data)

    