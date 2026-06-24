# Variables, Loops, Events, and Conditions

## Variables

A variable is a named container that holds a value.
The value can change while the program is running.

In a camera system, a variable might hold the confidence score of the 
last detection, or the count of how many frames have been processed.
The name stays the same. The value inside it changes.

example:
    frame_count = 0
    frame_count = frame_count + 1

## Loops

A loop repeats a block of instructions until some condition is met,
or forever if nothing tells it to stop.

A camera system runs in a loop. It does not check one frame and stop.
It keeps checking, frame after frame, as long as the system is on.

example:
    while camera_is_on:
        capture frame
        check for motion
        analyse if needed

## Events

An event is something that happens outside the normal flow of the program
and causes the program to react.

In Scratch, clicking the green flag is an event.
In a camera system, motion being detected is an event.
The program was not counting down to it. It just happened, and the 
system responded.

The difference between a loop and an event:
a loop checks repeatedly on its own schedule.
an event fires when something external triggers it.

## Conditions

A condition is a question the program asks that has a yes or no answer.
Based on the answer, the program takes a different path.

example:
    if confidence > 0.70:
        save the detection
    else:
        discard it

Conditions are what give a program decision-making ability.
Without conditions, every input would produce the same output.