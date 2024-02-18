import os
import sys
import requests

def download_xml(stopID):
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
    if len(sys.argv) != 2:
        print("Usage: python3 getXML.py <stopID>")
        sys.exit(1)
    
    stopID = sys.argv[1]
    download_xml(stopID)
