# week 4 - using pydantic to validate API data properly
# in api_contract.py I wrote manual checks with if statements
# pydantic does the same thing but cleaner and with better error messages
# it is the standard way to do this in FastAPI

from pydantic import BaseModel, ValidationError

# defining what a valid box looks like
class Box(BaseModel):
    x: int
    y: int
    width: int
    height: int

# defining what a valid detection looks like
class Detection(BaseModel):
    label: str
    confidence: float
    box: Box
    timestamp: str

# testing with valid data
valid_data = {
    "label": "person",
    "confidence": 0.91,
    "box": {"x": 10, "y": 20, "width": 50, "height": 100},
    "timestamp": "2024-01-15T10:30:00Z"
}

detection = Detection(**valid_data)
print(detection)
print(detection.label)
print(detection.box.width)

# testing with invalid data - confidence is a string instead of float
invalid_data = {
    "label": "person",
    "confidence": "high",
    "box": {"x": 10, "y": 20, "width": 50, "height": 100},
    "timestamp": "2024-01-15T10:30:00Z"
}

try:
    bad_detection = Detection(**invalid_data)
except ValidationError as e:
    print("\nvalidation failed:")
    print(e)

# testing with missing field
incomplete_data = {
    "label": "car",
    "box": {"x": 80, "y": 30, "width": 60, "height": 40},
    "timestamp": "2024-01-15T10:30:00Z"
}

try:
    bad_detection = Detection(**incomplete_data)
except ValidationError as e:
    print("\nvalidation failed:")
    print(e)