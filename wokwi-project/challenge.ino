#include "DHT.h"

#define DHTPIN 15     // Pino onde está ligado o DHT
#define DHTTYPE DHT22 // depois podemos colocar um sensor com melhor precisão

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(115200);
  dht.begin();
}

void loop()
{
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  if (isnan(temperatura) || isnan(umidade))
  {
    Serial.println("Falha ao ler o sensor DHT!");
    return;
  }

  unsigned long timestamp = millis();

  Serial.print("temperature_c: ");
  Serial.print(temperatura);
  Serial.print("°C | humidity_pct: ");
  Serial.print(umidade);
  Serial.print("% | timestamp: ");
  Serial.println(timestamp);

  delay(2000); // Lê a cada 2 segundos
}
