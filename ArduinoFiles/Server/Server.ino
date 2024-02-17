#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "ESPAsyncWebServer.h"
#include "ESPAsyncTCP.h"

// network params
const char* wifiname = "Intelligent Residence";
const char* ssid = "IntelligentResidence";
const char* password = "asdfasdfasdf";

AsyncWebServer server(80);

// TODO: functions for specific routes
String testRequest();

void setup() 
{
  Serial.begin(115200);
  
  WiFi.hostname(wifiname);

  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("Starting server at ");
  Serial.println(IP);

  server.on("/test", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/plain", testRequest());
  });
  
  server.begin();
}
 
void loop() 
{
  // nothing to do, async server
}

String testRequest() 
{
  return "YIPPIE";
}