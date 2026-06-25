# Blockly Games - Maze and Bird

## Maze section

The puzzle gives you a character that needs to reach a goal.
You connect blocks to tell it which direction to move.

What I noticed:
- You cannot write free text. Every instruction is a block you pick and connect.
- The program runs top to bottom unless you use a loop or condition.
- If the path has a turn, you need a condition to check direction before moving.

A working solution for a simple maze:

    move forward
    turn left
    move forward
    move forward

For a maze with a branch:

    repeat until goal reached:
        if path ahead:
            move forward
        else if path to the right:
            turn right
        else:
            turn left

## Bird section

The bird needs to reach the worm while avoiding the clouds.

What this added that maze did not have:
- A condition based on a value (angle, height) not just yes or no
- I had to think about ranges, not just directions

## What both exercises taught me

You can build real logic without typing a single character of code.
The constraint of only using available blocks forces you to think
about the exact steps rather than jumping to writing code.
This is the same thinking you need when designing a pipeline.