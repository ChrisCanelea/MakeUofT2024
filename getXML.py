import requests

# URL of the XML file
url = 'https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=0818'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response (the XML file)
    xml_content = response.content

    # Save the XML content to a file
    with open('busPrediction.xml', 'wb') as f:
        f.write(xml_content)
        
    print("XML file downloaded successfully.")
else:
    # If the request was not successful, print the status code
    print(f"Failed to download XML file. Status code: {response.status_code}")
