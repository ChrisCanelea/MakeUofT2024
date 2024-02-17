import os
import requests

# URL of the XML file
url = 'https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=0818'
# Path to the folder where you want to save the XML file
folder_path = './xml_files'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response (the XML file)
    xml_content = response.content

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the XML content to a file in the specified folder
    with open(os.path.join(folder_path, 'busPrediction.xml'), 'wb') as f:
        f.write(xml_content)
        
    print("XML file downloaded successfully.")
else:
    # If the request was not successful, print the status code
    print(f"Failed to download XML file. Status code: {response.status_code}")
