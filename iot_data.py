import random
import json
from datetime import datetime

def generate_sensor_data():
    timestamp = datetime.utcnow().isoformat()
    device_id = "iot_device_001"
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)

    data = {
        "device_id": device_id,
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }

    return data

def main():
    sensor_data = generate_sensor_data()
    json_data = json.dumps(sensor_data, indent=2)
    
    with open("iot_data.json", "w") as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    main()
