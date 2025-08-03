import paho.mqtt.client as mqtt
import json, time, socket, uuid, random

DEVICE_ID = "pi5_fake_sensor"
MQTT_BROKER = "3.82.147.85"
MQTT_PORT = 1883
TOPIC = f"devices/{DEVICE_ID}/data"

client_id = f"{DEVICE_ID}-{str(uuid.uuid4())[:8]}"
client = mqtt.Client(client_id)
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

while True:
    data = {
        "deviceId": DEVICE_ID,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "temperature": round(random.uniform(21, 29), 2),
        "hostname": socket.gethostname()
    }
    payload = json.dumps(data)
    print(f"📤 Publishing: {payload}")
    client.publish(TOPIC, payload)
    time.sleep(5)
