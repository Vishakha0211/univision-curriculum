# Camera Alert System - Flowchart Notes

## What I was trying to figure out
Before writing any code, I wanted to map out what a basic camera alert 
system would actually do. Like, what decisions does it make and in what order.

## The flowchart I drew

Start
  |
  v
Is motion detected?
  |           |
 Yes          No
  |           |
  v           v
Capture     Keep waiting
frame       (loop back)
  |
  v
Is the frame clear enough to analyse?
  |           |
 Yes          No
  |           |
  v           v
Send to     Discard frame
analysis    (loop back)
  |
  v
Done

## What I learned from drawing this

The system is basically just a series of yes/no questions.
Every decision either moves the process forward or sends it back to waiting.
This is what a loop looks like before you write it in code.

## The three concepts I had to explain

Data - the actual image pixels the camera captured. Raw information.

Command - an instruction like "capture frame" or "send for analysis". 
Something the system is told to do.

Event - motion being detected. Something that happens on its own 
and triggers the system to respond. The system wasn't told to check,
it just reacted.

The difference between a command and an event tripped me up at first.
A command is something you call. An event is something that calls you.
