# ~/mqtt_connect.py
import paho.mqtt.client as mqtt
import json
import time
import random
import socket
import uuid

# Change these!
BROKER = "3.82.147.85"       # your EC2 public IP
BROKER_PORT = 1883          # or 8883 if using TLS
DEVICE_ID = "pi5-demo"

TOPIC = f"devices/{DEVICE_ID}/data"
client_id = f"{DEVICE_ID}-{uuid.uuid4().hex[:8]}"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

client = mqtt.Client(client_id)
client.on_connect = on_connect

print(f"Connecting to {BROKER}:{BROKER_PORT} …")
client.connect(BROKER, BROKER_PORT, 60)
client.loop_start()

try:
    while True:
        payload = {
            "deviceId": DEVICE_ID,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "temperature": round(random.uniform(20,30),1),
            "humidity": round(random.uniform(30,70),1),
            "host": socket.gethostname()
        }
        print("Publishing:", payload)
        client.publish(TOPIC, json.dumps(payload))
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping…")
    client.loop_stop()
    client.disconnect()
