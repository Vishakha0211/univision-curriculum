# UI State Diagram - Detection Dashboard

## The three states

State 1: INCOMING
    What is visible: all detections, including low confidence ones
    How you get here: page loads, or user clicks "Incoming frames"
    What changes: the table shows every detection with a status badge

State 2: FILTERED
    What is visible: only detections above the 0.70 threshold
    How you get here: user clicks "Filtered results"
    What changes: table shrinks to only the kept detections

State 3: SUMMARY
    What is visible: aggregated numbers, no individual rows
    How you get here: user clicks "Summary"
    What changes: table disappears, stat boxes appear

## Transitions

INCOMING --> FILTERED   : user clicks "Filtered results" button
INCOMING --> SUMMARY    : user clicks "Summary" button
FILTERED --> INCOMING   : user clicks "Incoming frames" button
FILTERED --> SUMMARY    : user clicks "Summary" button
SUMMARY  --> INCOMING   : user clicks "Incoming frames" button
SUMMARY  --> FILTERED   : user clicks "Filtered results" button

## What stays the same across all states

The heading, subtitle, and the three stage buttons are always visible.
Only the panel content changes.
The active button is highlighted so the user knows which stage they are on.

## What I learned from drawing this out

Writing the states before building the HTML made the javascript much simpler.
I knew exactly what each button needed to do: deactivate everything,
then activate one panel and one button.
Without the diagram I would have written messier conditional logic.