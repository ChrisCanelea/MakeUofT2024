#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "ESPAsyncWebServer.h"
#include "ESPAsyncTCP.h"

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdfasdfasdf";

String result; // global string for getting time data from database
bool LEDon;

// create http server on port 80
AsyncWebServer server(80);

// Helper declaration
String toggleAppliances();
String outletStatus();
void decodeRequest(AsyncWebServerRequest *request);

void setup() 
{
  Serial.begin(921600);
  Serial.println("");

  LEDon = true;
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

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

  // handler for toggling appliances
  server.on("/appliances", HTTP_GET, [](AsyncWebServerRequest *request){
    // ack from appliance helper
    request->send(200, "text/plain", toggleAppliances());
  });

  // handler for the main terminal to get outlet status
  server.on("/update-outlets", HTTP_GET, [](AsyncWebServerRequest *request){
    // send outlet status from helper in form "<OUTL1status>:<OUTL2status>:<OUTL3Status>"
    request->send(200, "text/plain", outletStatus());
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

// function for toggling home appliances, modelled by LED on GPIO pins
String toggleAppliances() 
{
  digitalWrite(LED_BUILTIN, (LEDon)?(LOW):(HIGH));
  LEDon = !LEDon;

  return "ACK";
}

// function for returning outlet statuses
String outletStatus()
{
  // TODO: GPIO with 3 state switch

  return "ACK"; // temp
}
