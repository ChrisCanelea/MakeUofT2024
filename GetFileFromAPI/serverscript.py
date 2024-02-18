# Script that polls "server" ESP8266 for received HTTP requests over serial connection
# On success runs the "getSchedule.py" script to update the bus location database
# Sends the result back to the server over serial connection, where it can be queried

import serial
import subprocess

server = serial.Serial('COM7', 921600, timeout=1) # open server serial port

while True:
    data = server.readline() # data in form b'asdsfdgsdgf'

    # ignore empty strings (since polling)
    if data == b'':
        continue

    # check for our header of "/" (ASCII 47), otherwise ignore
    if data[0] != 47:
        continue

    data = data.decode('utf-8') # decode from serial (decode ASCII)
        
    if data[1] == "&": # route number query in form "/&<number>\r\n"
        route = data[2:-2] # discard first char, last 2 char
        print("Fetching stops on route: " + route) # debug print query

        # pass route number to data script
        # returns list of bus stations (stops) for a given route
        station_list = subprocess.check_output(["python","getStations.py",route])

        print(station_list.decode('utf-8')) # debug print result of route number query
        server.write(station_list) # send station list result back to server
    
    elif data[1] == "$": # station name query in form "/$<station name>\r\n"
        station = data[2:-2] # discard first char, last 2 char
        print("Fetching bus times for: " + station) # debug print query

        # pass station name to data script
        # returns bus times for previously queried route #
        bus_times = subprocess.check_output(["python","getSchedule.py",station])

        print(bus_times.decode('utf-8')) # debug print result of station name query
        server.write(bus_times) # send time result back to server