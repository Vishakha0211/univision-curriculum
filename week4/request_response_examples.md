# API Request and Response Examples

## Endpoint: POST /analyse

This is the endpoint the camera system calls when it has a frame ready.
It sends the image metadata and gets back a list of detections.

---

## Example request

POST /analyse
Content-Type: application/json

{
    "camera_id": "cam_03",
    "timestamp": "2024-01-15T10:30:00Z",
    "image": {
        "width": 1280,
        "height": 720,
        "format": "jpeg"
    }
}

---

## Example response - success

HTTP 200 OK
Content-Type: application/json

{
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

---

## Example response - validation error

HTTP 422 Unprocessable Entity
Content-Type: application/json

{
    "error": "validation_error",
    "detail": "field 'camera_id' is required but was not provided"
}

---

## Example response - server error

HTTP 500 Internal Server Error
Content-Type: application/json

{
    "error": "internal_error",
    "detail": "model inference failed"
}

---

## Status codes used and what they mean

200 - request worked, detections returned
422 - request was received but the data inside it was wrong or incomplete
500 - something broke on the server side, not the client's fault

## What I noticed

The request only sends metadata about the image, not the actual image bytes.
In a real system the image would either be sent as base64 encoded data
or the server would pull it from a storage location using a URL.
Sending raw image bytes in a JSON body is possible but gets complicated.