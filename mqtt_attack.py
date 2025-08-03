import paho.mqtt.client as mqtt
import time, json, socket, uuid

BROKER = "3.82.147.85"
PORT   = 1883
TOPIC  = "devices/pi5_fake_sensor/data"

client = mqtt.Client(f"attack-{str(uuid.uuid4())[:8]}")
client.connect(BROKER, PORT, 60)
client.loop_start()

print("🚨 Sending 120 messages with malformed JSON every 10th…")
for i in range(120):
    if i % 10 == 0:
        payload = '{"deviceId":"attack","malformed":true'   # no closing brace
    else:
        payload = json.dumps({
            "deviceId": "attack",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "value": i,
            "host": socket.gethostname()
        })
    client.publish(TOPIC, payload)
    time.sleep(0.5)

client.loop_stop()
client.disconnect()
