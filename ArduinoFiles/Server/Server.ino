#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "ESPAsyncWebServer.h"
#include "ESPAsyncTCP.h"

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdfasdfasdf";

String result;

AsyncWebServer server(80);

// TODO: functions for specific routes
// String testRequest();

void setup() 
{
  Serial.begin(115200);
  Serial.println("");

  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("Starting server at ");
  Serial.println(IP);

  server.on("/test", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/plain", testRequest());
  });
  server.on("/stations", HTTP_GET, [](AsyncWebServerRequest *request){
    // send stations list
    request->send(200, "text/plain", testRequest());
  });
  server.on("/time", HTTP_GET, [](AsyncWebServerRequest *request){
    // send time
    request->send(200, "text/plain", result);
  });
  
  // prepare for station time requests
  server.onNotFound(decodeRequest);

  server.begin();
}
 
void loop() 
{
  if (Serial.available() > 0)
  {
    // read the incoming string
    result = Serial.readString();
  }
}

String testRequest() 
{
  return "YIPPIE";
}

void decodeRequest(AsyncWebServerRequest *request) 
{
  Serial.println(request->url());    

  request->send(200, "text/plain", "Received");
}