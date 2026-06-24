# week 4 - understanding what an API contract means
# an API contract is basically an agreement about what data looks like
# when two parts of a system talk to each other
# if the detection model sends data to a dashboard, both sides need to
# agree on the structure, otherwise nothing works

# this is what I expect a single detection to look like
# I wrote it out as a dictionary first just to be clear about it

expected_structure = {
    "label": "string",
    "confidence": "float between 0 and 1",
    "box": "dictionary with x, y, width, height",
    "timestamp": "string in ISO format"
}

# now a function that checks if a real detection matches that structure

def is_valid_detection(detection):
    if "label" not in detection:
        print("missing: label")
        return False
    if "confidence" not in detection:
        print("missing: confidence")
        return False
    if "box" not in detection:
        print("missing: box")
        return False
    if "timestamp" not in detection:
        print("missing: timestamp")
        return False
    if not isinstance(detection["label"], str):
        print("wrong type: label should be a string")
        return False
    if not isinstance(detection["confidence"], float):
        print("wrong type: confidence should be a float")
        return False
    if not isinstance(detection["box"], dict):
        print("wrong type: box should be a dictionary")
        return False
    return True


# testing it on a valid detection
detection_1 = {
    "label": "person",
    "confidence": 0.91,
    "box": {"x": 10, "y": 20, "width": 50, "height": 100},
    "timestamp": "2024-01-15T10:30:00Z"
}

print(is_valid_detection(detection_1))

# testing it on a broken one - confidence is missing
detection_2 = {
    "label": "car",
    "box": {"x": 80, "y": 30, "width": 60, "height": 40},
    "timestamp": "2024-01-15T10:30:00Z"
}

print(is_valid_detection(detection_2))

# testing it on another broken one - label is a number not a string
detection_3 = {
    "label": 99,
    "confidence": 0.78,
    "box": {"x": 80, "y": 30, "width": 60, "height": 40},
    "timestamp": "2024-01-15T10:30:00Z"
}

print(is_valid_detection(detection_3))