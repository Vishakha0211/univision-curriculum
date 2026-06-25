# week 4 - building a tiny API using fastapi
# this is the first time the code actually listens for a real HTTP request
# instead of just functions you call yourself, this exposes an endpoint
# something else (postman, a browser, another service) can call it

# install first: pip install fastapi uvicorn pydantic

from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
from datetime import datetime

app = FastAPI()

# the data shape the API expects to receive
class Box(BaseModel):
    x: int
    y: int
    width: int
    height: int

class DetectionRequest(BaseModel):
    camera_id: str
    timestamp: str
    image_width: int
    image_height: int

# the data shape the API will return
class Detection(BaseModel):
    label: str
    confidence: float
    box: Box

class DetectionResponse(BaseModel):
    event_id: str
    camera_id: str
    timestamp: str
    detections: list[Detection]
    inference_time_ms: int

# a simple health check so you can confirm the server is running
@app.get("/health")
def health():
    return {"status": "ok"}

# the main endpoint
# it receives a request, pretends to run a model, and returns fake detections
# in a real system this would call yolo or another model
@app.post("/analyse", response_model=DetectionResponse)
def analyse(request: DetectionRequest):

    # pretend model output - hardcoded for now
    fake_detections = [
        Detection(
            label="person",
            confidence=0.91,
            box=Box(x=10, y=20, width=50, height=100)
        ),
        Detection(
            label="bicycle",
            confidence=0.72,
            box=Box(x=50, y=60, width=30, height=80)
        )
    ]

    # filter by confidence threshold
    threshold = 0.70
    filtered = [d for d in fake_detections if d.confidence >= threshold]

    response = DetectionResponse(
        event_id="evt_" + datetime.now().strftime("%H%M%S"),
        camera_id=request.camera_id,
        timestamp=request.timestamp,
        detections=filtered,
        inference_time_ms=34
    )

    return response

# to run this file:
# uvicorn fastapi_route:app --reload
#
# then open your browser at:
# http://127.0.0.1:8000/health        <- should return {"status": "ok"}
# http://127.0.0.1:8000/docs          <- fastapi gives you a built in test UI
#
# to test the /analyse endpoint use the docs page or postman
# send this as the request body:
# {
#     "camera_id": "cam_03",
#     "timestamp": "2024-01-15T10:30:00Z",
#     "image_width": 1280,
#     "image_height": 720
# }