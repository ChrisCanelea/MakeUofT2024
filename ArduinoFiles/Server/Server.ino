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

  // test handler, does nothing really
  server.on("/test", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/plain", testRequest());
  });

  // handler for returning a list of all stations
  server.on("/stations", HTTP_GET, [](AsyncWebServerRequest *request){
    // send stations list
    request->send(200, "text/plain", testRequest());
  });

  // handler for returning the time returned by the database, updated on time query
  server.on("/time", HTTP_GET, [](AsyncWebServerRequest *request){
    // send received time (received in main loop through serial connection to pc)
    request->send(200, "text/plain", result);
  });
  
  // notfound handler used for time query
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

// test function for http get requests, no longer used
String testRequest() 
{
  return "YIPPIE";
}

// function for handling time queries, called by notfound handler
void decodeRequest(AsyncWebServerRequest *request) 
{
  // forward the url string in form "/route_#:station_name\r\n" to script
  Serial.println(request->url());    

  // rudimentary ACK
  request->send(200, "text/plain", "Received");
}
