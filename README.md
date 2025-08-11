# IoT Security Threat Detection using Raspberry Pi, Suricata, and ELK on AWS

This repository contains Python scripts, which focuses on simulating and analyzing IoT MQTT traffic using a Raspberry Pi and an AWS-hosted security pipeline (Mosquitto, Suricata, Filebeat, Elasticsearch, Kibana).

## 🔧 Scripts

### 1. mqtt_connect.py
Simulates a temperature and humidity sensor publishing MQTT data with metadata.
- Sends JSON payloads to topic `devices/pi5-demo/data`.
- Includes hostname, random values, and timestamp.

### 2. mqtt_publisher.py
Similar to `mqtt_connect.py`, but simulates a simpler fake sensor.
- Publishes less metadata, focuses on temperature simulation.

### 3. mqtt_attack.py
- Simulates malicious MQTT traffic used for triggering Suricata rules.

## 🧪 Project Context

The scripts are meant to generate traffic that is:
- Ingested by Mosquitto broker on an AWS EC2 instance.
- Monitored by Suricata IDS.
- Parsed by Filebeat and visualized in Kibana.

## 📡 MQTT Broker

Ensure your EC2 Mosquitto broker is publicly accessible on port `1883`, and update `BROKER` or `MQTT_BROKER` IPs accordingly in each script.

## 🛠 Requirements

Install dependencies:
```bash
pip install paho-mqtt
