#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// WiFi Multi to send simultaneous requests
ESP8266WiFiMulti WiFiMulti;

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdf";

const char* serverNameTemp = "http://192.168.4.1/temperature";
const char* serverNameHumi = "http://192.168.4.1/humidity";
const char* serverNamePres = "http://192.168.4.1/pressure";

void setup() {
  Serial.begin(115200);
  Serial.println();

  // attempt to connect
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.println("Success");
}

void loop() 
{
  // ensure we are still connected
  if ((WiFiMulti.run() == WL_CONNECTED)) 
  {
    // send GET requests
    
  }
  else 
  {
    Serial.println("WiFi Disconnected");
  }
  
  Delay(5000);
}

String httpGETRequest(const char* url) {
  WiFiClient client;
  HTTPClient http;
  String payload; 
    
  // check for connection
  if (http.begin(client, url)) {
    
    // send http header
    int httpCode = http.GET();
    
    if (httpResponseCode > 0) 
    {
      Serial.print("HTTP response: ");
      Serial.println(httpResponseCode);
      payload = http.getString();
    }
    else 
    {
      Serial.println("GET FAILED");
    }

    http.end();

    return payload;
  } else 
  {
    Serial.println("HTTP failed to connect");
  }

  return "\0";
}