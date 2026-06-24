# a detection is not just one value, it has multiple pieces of info together
# label, confidence, and where in the image it was found (the box)
# a dictionary made sense for this

detection = {
    "label": "person",
    "confidence": 0.91,
    "box": {
        "x": 120,
        "y": 45,
        "width": 80,
        "height": 200
    }
}

# accessing values
print(detection["label"])
print(detection["confidence"])
print(detection["box"]["x"])

# I also tried making a list of multiple detections
# because in real use the model returns more than one

detections = [
    {
        "label": "person",
        "confidence": 0.91,
        "box": {"x": 120, "y": 45, "width": 80, "height": 200}
    },
    {
        "label": "car",
        "confidence": 0.55,
        "box": {"x": 300, "y": 100, "width": 150, "height": 90}
    },
    {
        "label": "bicycle",
        "confidence": 0.72,
        "box": {"x": 50, "y": 200, "width": 60, "height": 80}
    }
]

for d in detections:
    print(d["label"], d["confidence"])