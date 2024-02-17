import xml.sax  #simple api for xml

#handler = xml.sax.ContentHandler()
#parser = xml.sax.make_parser()
#parser.setContentHandler(handler)
#parser.parse('busSchedule.xml')

# https://retro.umoiq.com/xmlFeedDocs/NextBusXMLFeed.pdf

class BusHandler(xml.sax.ContentHandler):
    
    #define an element that triggers read
    def startElement(self, name, attrs):
        self.current = name
        


