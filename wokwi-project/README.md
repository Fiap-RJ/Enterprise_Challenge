# Monitoramento de Temperatura e Umidade com ESP32 e DHT22 🌡️Enterprise Challenge

**Nome do grupo**

### 👨‍🎓 Integrantes:

- Arthur Guimarães Alentejo
- Michael Rodrigues
- Nathalia Vasconcelos

### 👩‍🏫 Professores:

- **Tutor(a):** Lucas Gomes Moreira
- **Coordenador(a):** André Godoi

## Descrição do Projeto

Este projeto demonstra uma solução de Internet das Coisas (IoT) para o monitoramento em tempo real de temperatura e umidade, alinhada aos princípios da Indústria 4.0. Utilizando um microcontrolador ESP32 e um sensor DHT22, o sistema coleta dados do ambiente, que podem ser processados localmente e enviados para uma plataforma em nuvem para análise e visualização.

## Requisitos

```bash
arduino-cli
arduino-cli core update-index
arduino-cli core install esp32:esp32
arduino-cli lib install "DHT sensor library"
arduino-cli lib install "ESPAsyncWebServer"
arduino-cli lib install "AsyncTCP"
arduino-cli compile --fqbn esp32:esp32:esp32 --output-dir ./build
```

### Importância na Indústria 4.0

A utilização de sensores de temperatura e umidade na Indústria 4.0 não se trata apenas de medir condições ambientais, mas sim de uma estratégia inteligente para:

- Minimizar o tempo de inatividade dos equipamentos
- Reduzir os custos de manutenção (corretiva e preventiva)
- Aumentar a produtividade e a eficiência das operações
- Melhorar a qualidade dos produtos
- Garantir a segurança no ambiente de trabalho
- Tomar decisões mais estratégicas com base em dados em tempo real

Dessa forma, esses sensores são elementos chave para a digitalização e otimização dos processos industriais na era da Indústria 4.0.

## Simulação do Circuito

Abaixo estão as imagens da montagem do circuito em uma plataforma de simulação (Wokwi). A conexão é simples, utilizando uma porta digital do ESP32 para ler os dados do sensor DHT22.

![Descrição](/wokwi-project/assets/circuto.png)

### Esquema de Ligação:

- **Pino VCC do DHT22** → Pino 5V5 do ESP32
- **Pino GND do DHT22** → Pino GND do ESP32
- **Pino de Dados do DHT22** → Pino D15 do ESP32

### Print da Simulação:

![Descrição](/wokwi-project/assets/simulacao-circuito.jpg)

## Componentes Utilizados

| Componente       | Justificativa da escolha                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ESP32**        | Escolhido por seu excelente custo-benefício, processador dual-core e, principalmente, por sua conectividade Wi-Fi e Bluetooth nativa. Essas características são essenciais para projetos de IoT, permitindo que os dados sejam facilmente enviados para plataformas em nuvem (como AWS, Azure ou Google Cloud) sem a necessidade de módulos adicionais, o que é crucial para a digitalização do chão de fábrica. |
| **Sensor DHT22** | Este sensor é popular em projetos de prototipagem devido à sua boa precisão para medições de temperatura e umidade, interface digital simples (um fio) e baixo custo. É ideal para monitorar condições ambientais em ambientes controlados como um chão de fábrica, estufas ou data centers.                                                                                                                     |

## Comportamento da Simulação

A seguir, um exemplo da saída de dados visualizada no Monitor Serial da IDE Arduino ou do simulador. Os dados são exibidos a cada 2 segundos, conforme definido no código, simulando a coleta contínua em um ambiente de fábrica.

_[Inserir print do Monitor Serial com os dados sendo exibidos aqui]_

### Exemplo de Saída:

```
Iniciando monitoramento com DHT22!
humidity_pct: 55.40%  |  temperature_c: 23.80 *C
humidity_pct: 55.40%  |  temperature_c: 23.90 *C
humidity_pct: 55.30%  |  temperature_c: 23.90 *C
...
```

## Análise Exploratória e Insights Iniciais 📊

Após a coleta de dados por meio de **simulação**, estes foram importados para jupyter e gerada análise utilizando ferramentas em Python com Panda/Matplotlib/Seaborn com gráficos para extrair insights valiosos para o processo industrial.

### Série Temporal (Line Plot)
#### Objetivo: Visualizar a variação de temperatura e umidade ao longo do tempo.
![Gráfico de linha com duas variáveis](/wokwi-project/assets/grafico_linha_temp_umid.png)
---
### Histograma
#### Objetivo: Ver a distribuição dos valores de temperatura e umidade.
![Distribuição de temperatura e umidade](/wokwi-project/assets/histograma_temp_umid.png)
---
### Média Móvel
#### Objetivo: Suavizar a série de temperatura para facilitar a visualização de tendências e padrões ao longo do tempo.
![Variação da média de temperatura](/wokwi-project/assets/media_movel_temperatura.png)


### Insights Iniciais:

**Variação de Temperatura e Umidade:** Os gráficos de linha podem revelar padrões diários ou sazonais na temperatura e umidade do chão de fábrica. Picos ou quedas abruptas podem indicar eventos específicos, como a abertura de grandes portas, o acionamento de sistemas de ventilação, ou a operação de máquinas que geram calor excessivo.

**Histograma:** O histograma é fundamental para entender a frequência com que certos valores ocorrem, permitindo avaliar a estabilidade das variáveis monitoradas. Essa análise auxilia na identificação de faixas de operação mais comuns, na detecção de possíveis outliers e no suporte à calibração de sensores e sistemas automatizados. É especialmente útil para validar se o ambiente está operando dentro dos parâmetros ideais definidos.

**Média móvel:** A aplicação de médias móveis permite uma visão mais clara das tendências gerais, eliminando ruídos de variações pontuais. Essa técnica é amplamente usada para acompanhar a evolução de variáveis com o tempo e é valiosa para apoiar decisões baseadas em comportamento histórico. Também pode ser usada como referência para estabelecer limites operacionais dinâmicos e acompanhar a eficácia de ações corretivas ao longo dos dias ou semanas.

**Otimização de Processos:** Ao analisar os dados ao longo do tempo, pode-se identificar condições ambientais ótimas para determinados processos de fabricação, otimizando o consumo de energia dos sistemas de climatização ou a qualidade do produto final.

## Funcionamento do Sistema

O sistema de monitoramento de temperatura e umidade opera em um fluxo contínuo e automatizado, integrando hardware e software para fornecer dados em tempo real:

### 1. Coleta de Dados

O sensor DHT22, posicionado estrategicamente no ambiente a ser monitorado (ex: chão de fábrica), mede a temperatura e a umidade relativa do ar. Essas medições são convertidas em sinais elétricos digitais.

### 2. Processamento Local

O microcontrolador ESP32 está programado para ler periodicamente os sinais digitais do DHT22. O firmware embarcado no ESP32 decodifica esses sinais, aplicando as fórmulas necessárias para converter os dados brutos em valores legíveis de temperatura (em Celsius) e umidade (em porcentagem). O ESP32 também pode realizar validações básicas dos dados, descartando leituras inválidas.

### 3. Visualização Local (Depuração)

Para fins de desenvolvimento, depuração e monitoramento inicial, os dados processados são exibidos no Monitor Serial da IDE Arduino. Isso permite aos desenvolvedores e operadores verificar o funcionamento do sistema em tempo real, sem a necessidade de uma infraestrutura de nuvem completa.

### 4. (Próximo Passo) Conexão com a Nuvem

Uma vez que os dados são lidos e processados localmente, o ESP32, devido à sua capacidade de conectividade Wi-Fi nativa, pode se conectar a uma rede local. A partir daí, ele pode enviar os dados de temperatura e umidade para uma plataforma de dados em nuvem. Isso é tipicamente feito usando protocolos de IoT como MQTT (Message Queuing Telemetry Transport) para mensagens leves e eficientes, ou HTTP para requisições mais diretas. As plataformas de nuvem, como AWS IoT Core, Google Cloud IoT, Azure IoT Hub, ou serviços como Adafruit IO e Thingspeak, são ideais para isso.

### 5. Armazenamento, Análise e Tomada de Decisão (Na Nuvem)

Uma vez na nuvem, os dados são armazenados de forma segura em bancos de dados escaláveis. Eles podem então ser processados por serviços de análise de dados, visualizados em dashboards interativos (permitindo que gestores e engenheiros monitorem as condições remotamente) e até mesmo serem usados para acionar alertas automatizados (ex: SMS, e-mail) se os valores excederem limites predefinidos. Algoritmos de Machine Learning podem ser aplicados para prever falhas em equipamentos ou otimizar processos, contribuindo para a manutenção preditiva e a otimização operacional características da Indústria 4.0.
