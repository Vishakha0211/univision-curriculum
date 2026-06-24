# the model returns all detections including low confidence ones
# I need a way to keep only the ones above a certain threshold
# built this step by step

detections = [
    {"label": "person",  "confidence": 0.91, "box": {"x": 120, "y": 45,  "width": 80,  "height": 200}},
    {"label": "car",     "confidence": 0.55, "box": {"x": 300, "y": 100, "width": 150, "height": 90}},
    {"label": "bicycle", "confidence": 0.72, "box": {"x": 50,  "y": 200, "width": 60,  "height": 80}},
    {"label": "dog",     "confidence": 0.40, "box": {"x": 90,  "y": 50,  "width": 25,  "height": 30}},
]

# first I did it manually just to see what was happening
kept = []
for d in detections:
    if d["confidence"] >= 0.70:
        kept.append(d)

print("kept manually:")
for d in kept:
    print(d["label"], d["confidence"])

# then I made it a function so the threshold can change
def filter_detections(detections, threshold):
    result = []
    for d in detections:
        if d["confidence"] >= threshold:
            result.append(d)
    return result

filtered = filter_detections(detections, 0.70)
print("\nkept via function:")
for d in filtered:
    print(d["label"], d["confidence"])