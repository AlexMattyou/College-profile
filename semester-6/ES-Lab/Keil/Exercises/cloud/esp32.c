#include <WiFi.h>
#include "DHT.h"
#include "HTTPClient.h"

#define DHTPIN 15
#define DHTTYPE DHT11

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

String apiKey = "YOUR_THINGSPEAK_API_KEY";
const char* server = "http://api.thingspeak.com/update";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println(" Connected!");
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature(); // Read Celsius
  if (isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.println(temp);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = server + String("?api_key=") + apiKey + "&field1=" + String(temp);
    http.begin(url);
    int httpCode = http.GET();
    http.end();

    Serial.print("HTTP Response Code: ");
    Serial.println(httpCode);
  }

  delay(15000); // ThingSpeak limit
}
