import xml.dom.minidom
import sys
import requests
import os

# https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf

#this function parse the xml file and output the schedule
def outSchedule():
    domtree = xml.dom.minidom.parse('./xml_files/stopPrediction.xml')
    group = domtree.documentElement
    predictions = group.getElementsByTagName('prediction')

    for prediction in predictions:
        # epochTime = prediction.getAttribute('epochTime')
        # min = prediction.getAttribute('minutes')
        sec = prediction.getAttribute('seconds')
        print(f"{sec}")

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
            
        #print("XML file downloaded successfully.")
    else:
        # If the request was not successful, print the status code
        print(f"Failed to download XML file. Status code: {response.status_code}")

def getStationId(stationName):
    #we check if the station exist in the LUT
    domtree = xml.dom.minidom.parse('./xml_files/busStopLUT.xml')
    group = domtree.documentElement
    stops = group.getElementsByTagName('stop')
    #check if busID is in the LUT
    for stop in stops:
        title = stop.getAttribute('title')
        tag = stop.getAttribute('tag')
        if stationName == title and tag[-3:]!="_ar":
            return stop.getAttribute('stopId')
    
    print("No station match")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 getSchedule.py <station name>")
        sys.exit(1)
    
    stationName = sys.argv[1]

    stopId = getStationId(stationName)
    getPrediction(stopId)
    outSchedule()
