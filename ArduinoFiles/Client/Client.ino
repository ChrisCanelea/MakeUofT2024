#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// WiFi Multi to send simultaneous requests
ESP8266WiFiMulti WiFiMulti;

// network params
const char* ssid = "IntelligentResidence";
const char* password = "asdfasdfasdf";

const char* testURL = "http://192.168.4.1/test";

void setup() {
  Serial.begin(115200);
  Serial.println();

  // attempt to connect
  // WiFi.begin(ssid, password);
  // while (WiFi.status() != WL_CONNECTED) {
  //   delay(500);
  // }

  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println("Success");
}

void loop() 
{
  // ensure we are still connected
  if ((WiFiMulti.run() == WL_CONNECTED)) 
  {
    // send GET requests
    String result = httpGETReq(testURL);

    if (result != "\0") 
    {
      // do something with result

    }
  }
  else 
  {
    Serial.println("WiFi Disconnected");
  }
  
  delay(5000);
}

String httpGETReq(const char* url) {
  WiFiClient client;
  HTTPClient http;
  String payload; 
    
  // check for connection
  if (http.begin(client, url)) {
    
    // send http header
    int httpCode = http.GET();
    
    if (httpCode > 0) 
    {
      Serial.print("HTTP payload: ");
      payload = http.getString();
      Serial.println(payload);
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