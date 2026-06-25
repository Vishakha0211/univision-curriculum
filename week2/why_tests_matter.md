# Why Tests Matter Before a System Gets Complicated

## The problem without tests

When I wrote filter_detections, it was one small function.
I could run it and check the output by reading it myself.
That works when there is one function.

Imagine the system grows:
- filter_detections feeds into a risk scorer
- the risk scorer feeds into an alert system
- the alert system writes to a database

Now if filter_detections has a bug, the alert is wrong,
the database entry is wrong, and nothing tells you where it broke.
You find out at the end when the output is obviously wrong.
By then the bug could be anywhere.

## What a test does

A test checks one specific thing and tells you immediately if it breaks.

    def test_at_threshold():
        data = [{"label": "cat", "confidence": 0.70, "box": {}}]
        result = filter_detections(data, 0.70)
        assert len(result) == 1

If someone later changes the function to use > instead of >=,
this test fails instantly and points directly at the problem.

## The second reason tests matter

Tests force you to think about edge cases before they become bugs.
When I wrote the empty list test, I had not actually checked
whether my function would crash on an empty list.
Writing the test made me check. It did not crash, but now I know for certain.

## The third reason

Tests are documentation that cannot go out of date.
A comment saying "this filters below the threshold" can be wrong.
A passing test proving it cannot be wrong.