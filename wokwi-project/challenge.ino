#include <WiFi.h>
#include <DHT.h>
#include <ESPAsyncWebServer.h>

#define DHTPIN 15
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
AsyncWebServer server(80);

// Wi-Fi
const char *ssid = "SEU_WIFI";
const char *password = "SUA_SENHA";

void setup()
{
    Serial.begin(115200);
    dht.begin();

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Conectando ao Wi-Fi...");
    }

    Serial.println(WiFi.localIP());

    server.on("/dados", HTTP_GET, [](AsyncWebServerRequest *request)
              {
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    if (isnan(t) || isnan(h)) {
      request->send(500, "application/json", "{\"erro\":\"Falha ao ler o sensor\"}");
      return;
    }
    String json = "{\"temperatura\":" + String(t) + ",\"umidade\":" + String(h) + "}";
    request->send(200, "application/json", json); });

    server.begin();
}
