# HTTP Status Codes - What They Mean in an API

## Why status codes matter

When two systems talk over HTTP, the status code is the first thing
the receiving side checks. Before it reads any data, it checks the code.
A 200 means read the response. A 422 means the request was wrong.
A 500 means something broke on the server.

If you do not return the right code, the other system cannot handle
errors correctly. It might treat a failed request as a success.

## The codes this API uses

200 OK
    The request worked. The response contains the detection results.
    The client should read the detections and process them.

422 Unprocessable Entity
    The request arrived but the data inside it was wrong or incomplete.
    FastAPI and Pydantic return this automatically if a required field
    is missing or has the wrong type.
    The client sent something malformed. It is the client's fault.

500 Internal Server Error
    Something broke on the server side while processing the request.
    The model crashed, a file was missing, memory ran out.
    It is not the client's fault.
    The server should log this. The client should retry or alert someone.

## What I tested in Postman

Request 1 - valid request
    POST /analyse with all required fields
    Result: 200, two detections returned

Request 2 - missing camera_id
    POST /analyse without camera_id
    Result: 422, fastapi returned a clear error message automatically
    I did not have to write any error handling code for this

Request 3 - wrong type for image_width
    Sent image_width as a string "wide" instead of an integer
    Result: 422, pydantic caught it before my function even ran

## What I would add in a real system

408 Request Timeout - if the model takes too long
401 Unauthorized - if the request does not have a valid API key
404 Not Found - if the endpoint path is wrong
429 Too Many Requests - if the client is sending too fast