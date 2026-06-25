# Midterm Report
### UniVision Concept Learning Curriculum
**Student:** Vishakha Arekar
**Program:** UniVision
**Period:** Weeks 1 to 4

---

## Overview

So this is my midterm report covering the first four weeks of the UniVision curriculum. Honestly when I started I was a bit nervous because I had not done proper structured programming before. But the curriculum was designed in a way where you build up slowly and that really helped. Each week had a different focus and by the end of week 4 I felt like things were actually connecting together.

All my work is pushed to my GitHub repo: [github.com/Vishakha0211/univision-curriculum](https://github.com/Vishakha0211/univision-curriculum)

---

## Week 1: Computing Without Fear

This week was about understanding how computers think before writing any actual code. The idea was to get comfortable with logic, flowcharts, and events.

I used Scratch and Blockly which are visual tools where you drag blocks instead of typing code. At first it felt too simple but I quickly understood why we started here. When you are dragging blocks you cannot just write vague logic, you have to be really precise about what happens step by step. That was the actual lesson.

**What I built and did:**

I made a Scratch sprite that moves when you press a key and stops at the edge of the screen. Sounds simple but it made me understand what an event listener actually is. It is not the same as a loop that keeps checking. It just sits and waits for something to happen.

I also drew a flowchart for a camera alert system. Like if motion is detected then capture the frame and check quality, otherwise keep waiting. Drawing this out made it very clear how a real system makes decisions.

One thing the curriculum asked us to do was write a plain language algorithm for deciding whether an image even needs to be sent to an AI model. I wrote that out and included the idea of failing fast, meaning you check simple things first before doing expensive things like calling a model.

**Files committed:** scratch_project_notes.md, blockly_notes.md, flowchart_notes.md, algorithm_notes.md, homework_concepts.md

---

## Week 2: Python as a Tool

This week we actually wrote Python. The approach was to not jump straight to fancy built in functions but to first do things manually and then clean them up.

**What I built and did:**

I wrote a function that takes a list of confidence scores from a detection model and returns the average. I first did it with a manual loop and then refactored it into a proper reusable function.

I also learned about dictionaries by representing a single detection as a dictionary with fields like label, confidence, and bounding box. Then I extended it to a list of multiple detections which is closer to what a real system would return.

The most useful thing this week was writing a filter function that removes detections below a confidence threshold. Again I wrote the manual version first before making it a function.

Then I wrote four tests for it covering normal cases, edge cases like an empty list, and exact threshold matching. Writing tests felt annoying at first but then I understood the point. Once your code grows you cannot manually check everything every time. Tests do that for you.

**Files committed:** confidence_scores.py, detection_dict.py, filter_detections.py, test_filter.py, why_tests_matter.md

---

## Week 3: Web Basics and React

This week moved into web development. HTML, CSS, JavaScript, TypeScript, and then React. A lot of ground to cover but again it was broken into steps.

**What I built and did:**

I built a basic HTML and CSS page that displays detection results as styled cards. Nothing fancy but it was my first time actually laying out a webpage from scratch.

Then I built a three card stage page showing Input, Detection, and Output stages with status that changes when you interact with it. This was done in plain JavaScript first to understand what is actually happening with state before moving to React.

The React part was really interesting. I built a pipeline events component where you can see events, filter them by status, and add new ones. Using useState in React felt a bit confusing at first but once I had the plain JavaScript version to compare it to, it clicked.

I also converted my Week 2 data structures into TypeScript types which forces you to be explicit about what shape your data is in. That was a good exercise.

One thing that is still in progress is the full MDN JavaScript section. I have been going through it but have not finished everything yet. I noted this as pending.

**Files committed:** basics.html, js_practice.js, stage_cards.html, dashboard.html, types.ts, PipelineEvents.jsx, ui_state_diagram.md

---

## Week 4: APIs and JSON Contracts

This week was about APIs, how they are designed, how data is validated, and how errors are communicated properly.

**What I built and did:**

I started by designing an API contract manually using if statements to understand what validation actually is before using any library. Then I rewrote the same validation using Pydantic which is a Python library that handles all of that cleanly.

I also studied JSON properly, things like nested objects, arrays, and metadata, and the difference between json.dumps and json.loads which is basically the difference between turning Python into JSON text and turning JSON text back into Python.

The main thing I built was a working FastAPI route with a health check endpoint and a POST /analyse endpoint that accepts a camera request and returns detection results. I tested this using the automatic docs page that FastAPI generates and also in Postman.

In Postman I tested four scenarios: a valid request, a request with a missing field, a request with the wrong data type, and the health check. I documented what I expected and what actually came back.

I also wrote up the status codes 200, 422, and 500 in plain language including whose fault each one is. That framing actually helped me understand them better.

Note: Week 4 overlapped with DAV team training so some of it was done alongside that work. The computer vision and deep learning module that extends from Week 4 is still ongoing.

**Files committed:** api_contract.py, pydantic_validation.py, json_schema.py, fastapi_route.py, postman_notes.md, status_codes.md, request_response_examples.md

---

## Overall Thoughts

Looking back at four weeks of work the thing I am most proud of is that the code files actually show the learning process. Early files are messier and more manual. Later files are cleaner and more abstracted. That was the intention of the curriculum and I tried to follow it honestly rather than jumping straight to polished solutions.

The connection between weeks also started to make sense by the end. Week 1 taught me to think in steps. Week 2 gave me Python to express those steps. Week 3 gave me a way to display the results on screen. Week 4 gave me a way to expose the logic as an API. It is the same camera detection problem, just seen from different angles each week.

Still pending: finishing the MDN JavaScript section from Week 3 and completing the extended computer vision module from Week 4.

---

*Repository: [github.com/Vishakha0211/univision-curriculum](https://github.com/Vishakha0211/univision-curriculum)*
