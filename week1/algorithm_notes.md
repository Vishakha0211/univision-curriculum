# Deciding Whether an Image Needs Analysis

## The problem I was thinking about

Not every frame a camera captures is worth analysing. 
If you send everything to a model, you waste compute and time.
So I tried to write out the logic for filtering frames before analysis.

## My plain language algorithm

1. A new frame comes in from the camera
2. Check if it was triggered by motion
   - If no motion triggered it, skip the frame and go back to step 1
3. Check if the image is usable
   - Too dark, too blurry, or too small means skip it
   - Log that it was skipped so we know it happened
4. If the image looks fine, pass it to the detection model
5. Log what came back: the label, confidence score, and time

## Why I wrote it this way

I noticed that most frames would get filtered out early.
Steps 2 and 3 are cheap checks. The model call in step 4 is expensive.
So you want to fail fast and only reach step 4 when you have to.

This is the same idea as checking if a list is empty before looping through it.
No point doing work on something that has nothing in it.

## What I still want to understand

How does the camera know motion happened in the first place?
That must be handled somewhere before this algorithm even starts.
Probably a separate sensor or a frame difference calculation.
I want to look into that when we get to the OpenCV section.