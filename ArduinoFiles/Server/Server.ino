#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "ESPAsyncWebServer.h"
#include "ESPAsyncTCP.h"

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdfasdfasdf";

// global string for getting time data from database
String result;

// create http server on port 80
AsyncWebServer server(80);

void setup() 
{
  Serial.begin(115200);
  Serial.println("");

  // create soft access point
  WiFi.softAP(ssid, password);

  // print ip in case it changes, should be 192.168.4.1 consistently though
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Starting server at ");
  Serial.println(IP);

  // Handlers

  // handler for testing another ESP8266 device as a client
  server.on("/test", HTTP_GET, [](AsyncWebServerRequest *request){
    // send basic string response
    request->send(200, "text/plain", "YIPPIE");
  });

  // handler for getting the result of a query
  server.on("/result", HTTP_GET, [](AsyncWebServerRequest *request){
    // send received string (received in main loop through serial connection to pc)
    request->send(200, "text/plain", result);
  });
  
  // notfound handler used for a query
  server.onNotFound(decodeRequest);

  // end setup
  server.begin();
}
 
void loop() 
{
  // poll for serial messages from pc script
  if (Serial.available() > 0)
  {
    // read the incoming string from database
    result = Serial.readString();
  }
}

// function for handling time queries, called by notfound handler
void decodeRequest(AsyncWebServerRequest *request) 
{
  // forward the url string in form "/route_#:station_name\r\n" to script
  Serial.println(request->url());    

  // rudimentary ACK
  request->send(200, "text/plain", "Received");
}
