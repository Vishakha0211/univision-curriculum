# week 4 - working with JSON
# JSON is how most APIs send and receive data
# I wanted to understand how to build it, send it, and read it back

import json

# building a full detection event from scratch
# this is what the camera system might send after processing a frame

event = {
    "event_id": "evt_001",
    "camera_id": "cam_03",
    "timestamp": "2024-01-15T10:30:00Z",
    "detections": [
        {
            "label": "person",
            "confidence": 0.91,
            "box": {"x": 10, "y": 20, "width": 50, "height": 100}
        },
        {
            "label": "bicycle",
            "confidence": 0.72,
            "box": {"x": 50, "y": 60, "width": 30, "height": 80}
        }
    ],
    "metadata": {
        "model": "yolov8",
        "inference_time_ms": 34
    }
}

# converting the dictionary to a JSON string
# this is what actually gets sent over a network
json_string = json.dumps(event)
print("as a string:")
print(json_string)

# pretty version - easier to read
print("\npretty printed:")
print(json.dumps(event, indent=2))

# converting it back from a string to a dictionary
# this is what the receiving side does
received = json.loads(json_string)
print("\nreading values back out:")
print(received["camera_id"])
print(received["metadata"]["model"])
print("number of detections:", len(received["detections"]))

# looping through detections from the received data
print("\ndetections received:")
for d in received["detections"]:
    print(d["label"], "-", d["confidence"])

# one thing I noticed: json.dumps turns it into a string
# json.loads turns a string back into a dictionary
# dumps = dictionary out (to string), loads = load string (to dictionary)
# I had to look this up because the names are not obvious