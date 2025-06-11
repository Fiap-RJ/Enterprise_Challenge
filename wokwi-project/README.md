requeriments

- arduino-cli
- arduino-cli core update-index
- arduino-cli core install esp32:esp32
- arduino-cli lib install "DHT sensor library"
- arduino-cli lib install "ESPAsyncWebServer"
- arduino-cli lib install "AsyncTCP"
- arduino-cli compile --fqbn esp32:esp32:esp32 --output-dir ./build
