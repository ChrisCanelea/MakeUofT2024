import xml.dom.minidom
import sys
import subprocess
import requests
import os

# https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf

#this function parse the xml file and output the schedule
def outSchedule():
    domtree = xml.dom.minidom.parse('./xml_files/stopPrediction.xml')
    group = domtree.documentElement
    predictions = group.getElementsByTagName('prediction')

    for prediction in predictions:
        epochTime = prediction.getAttribute('epochTime')
        sec = prediction.getAttribute('seconds')
        min = prediction.getAttribute('minutes')
        print(f"epochTime: {epochTime}, min: {min}, sec: {sec}")


def getBusStops(busID):
    # Send an HTTP GET request to the URL
    body = 'https://retro.umoiq.com/service/publicXMLFeed?command=routeConfig&a=ttc&r='
    url = body+busID
    response = requests.get(url)

    folder_path = './xml_files'

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        xml_content = response.content
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Save the XML content to a file in the specified folder
        with open(os.path.join(folder_path, 'busStopLUT.xml'), 'wb') as f:
            f.write(xml_content)
            
        print("XML file downloaded successfully.")
    else:
        # If the request was not successful, print the status code
        print(f"Failed to download XML file. Status code: {response.status_code}")


#this function takes the busID, station name and check if they are valid
def checkBusId(busID):
    idIsValid = False

    #we check if the bus id exist in the LUT
    domtree = xml.dom.minidom.parse('./xml_files/ttcLUT.xml')
    group = domtree.documentElement
    routes = group.getElementsByTagName('route')
    #check if busID is in the LUT
    for route in routes:
        tag = route.getAttribute('tag')
        if busID == tag:
            idIsValid = True
            break

    # if the bus id is valid, get bus stop from API 
    if idIsValid:
        getBusStops(busID)
    #if not, return error
    else:
        print("Bus ID is not valid")
        sys.exit(1)

def getStationId(stationName):
    #we check if the station exist in the LUT
    domtree = xml.dom.minidom.parse('./xml_files/busStopLUT.xml')
    group = domtree.documentElement
    stops = group.getElementsByTagName('stop')
    #check if busID is in the LUT
    for stop in stops:
        title = stop.getAttribute('title')
        if stationName == title:
            return stop.getAttribute('stopId')
    
    print("No station match")
    sys.exit(1)

def getPrediction(stopID):
    # Send an HTTP GET request to the URL
    body = 'https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a=ttc&stopId='
    url = body+stopID
    response = requests.get(url)

    folder_path = './xml_files'

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        xml_content = response.content

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Save the XML content to a file in the specified folder
        with open(os.path.join(folder_path, 'stopPrediction.xml'), 'wb') as f:
            f.write(xml_content)
            
        print("XML file downloaded successfully.")
    else:
        # If the request was not successful, print the status code
        print(f"Failed to download XML file. Status code: {response.status_code}")
 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 getSchedule.py <bus #> <station name>")
        sys.exit(1)
    
    busID = sys.argv[1]
    stationName = sys.argv[2]

    checkBusId(busID)
    stopId = getStationId(stationName)
    getPrediction(stopId)
    outSchedule()
