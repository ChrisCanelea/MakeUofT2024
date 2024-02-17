#include <ESP8266WiFi.h>
#include <ESPAsyncWebServer.h>

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdf";

AsyncWebServer server(80);

// TODO: functions for specific routes

void setup() 
{
  Serial.begin(115200);
  Serial.println();
  
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("Starting server at ");
  Serial.println(IP);

  server.on("/temperature", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readTemp().c_str());
  });
  server.on("/humidity", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readHumi().c_str());
  });
  server.on("/pressure", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readPres().c_str());
  });
  
  server.begin();
}
 
void loop() 
{
  
}
