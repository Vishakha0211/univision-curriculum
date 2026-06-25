# Scratch Project - Event Driven Sprite

## What I built

A sprite that moves when arrow keys are pressed and stops at the edge of the screen.

## How I thought about it before building

I had to figure out what should trigger movement and what should stop it.
The trigger is a keypress. The stop condition is hitting the edge.
These are two separate things and they run independently.

## The blocks I used

when [right arrow] key pressed
    move 10 steps
    if on edge, bounce

when [left arrow] key pressed
    point in direction -90
    move 10 steps
    if on edge, bounce

when [up arrow] key pressed
    point in direction 0
    move 10 steps
    if on edge, bounce

when [down arrow] key pressed
    point in direction 180
    move 10 steps
    if on edge, bounce

## What I learned

Each "when key pressed" block is an event listener.
The sprite does not check the keyboard constantly.
It waits and reacts.
This is the same idea behind button clicks in a web page
or motion triggers in a camera system.

## What confused me

At first I thought I needed one big loop checking all keys.
But Scratch handles multiple events at the same time naturally.
I did not need a loop at all for the basic version.