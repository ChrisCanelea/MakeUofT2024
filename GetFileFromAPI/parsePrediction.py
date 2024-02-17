import xml.dom.minidom

# https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf

domtree = xml.dom.minidom.parse('./xml_files/busPrediction.xml')

group = domtree.documentElement
predictions = group.getElementsByTagName('prediction')

for prediction in predictions:
    epochTime = prediction.getAttribute('epochTime')
    sec = prediction.getAttribute('seconds')
    min = prediction.getAttribute('minutes')
    print(f"epochTime: {epochTime}, min: {min}, sec: {sec}")






