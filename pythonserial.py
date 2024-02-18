# Skeleton code for receiving Serial input
import serial
import time

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
        print("SUCCESS")
        # parse data string and get arrival/departure time of next bus

        server.write(b'Success') # send result back to server
    
    print(data)

    