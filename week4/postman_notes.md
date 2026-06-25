# Testing the API with Postman

## Setup

1. Download Postman from postman.com
2. Run the fastapi server first:
   uvicorn fastapi_route:app --reload
3. Open Postman

## Test 1 - health check

Method: GET
URL: http://127.0.0.1:8000/health

Expected response:
{
    "status": "ok"
}

Result: 200 OK

## Test 2 - valid analyse request

Method: POST
URL: http://127.0.0.1:8000/analyse
Headers: Content-Type: application/json
Body:
{
    "camera_id": "cam_03",
    "timestamp": "2024-01-15T10:30:00Z",
    "image_width": 1280,
    "image_height": 720
}

Expected response:
{
    "event_id": "evt_103000",
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
    "inference_time_ms": 34
}

Result: 200 OK

## Test 3 - missing required field

Method: POST
URL: http://127.0.0.1:8000/analyse
Body:
{
    "timestamp": "2024-01-15T10:30:00Z",
    "image_width": 1280,
    "image_height": 720
}

camera_id is missing.

Result: 422 Unprocessable Entity
FastAPI returned the error automatically. I did not write any error
handling code. Pydantic caught it before the function ran.

## Test 4 - wrong data type

Method: POST
URL: http://127.0.0.1:8000/analyse
Body:
{
    "camera_id": "cam_03",
    "timestamp": "2024-01-15T10:30:00Z",
    "image_width": "wide",
    "image_height": 720
}

image_width is a string instead of an integer.

Result: 422 Unprocessable Entity

## What I noticed

The FastAPI /docs page at http://127.0.0.1:8000/docs lets you
test every endpoint directly in the browser without Postman.
It reads the Pydantic models and builds the form automatically.
This is called automatic API documentation and it comes free with FastAPI.