# before this I had never written a test
# the reason tests matter: once the system grows, you can not manually
# check every function every time something changes
# a test does that check for you automatically

# copying the function here so the test file is self contained
def filter_detections(detections, threshold):
    result = []
    for d in detections:
        if d["confidence"] >= threshold:
            result.append(d)
    return result


# test 1 - normal case, some above and some below
def test_basic_filter():
    data = [
        {"label": "person", "confidence": 0.91, "box": {}},
        {"label": "car",    "confidence": 0.55, "box": {}},
    ]
    result = filter_detections(data, 0.70)
    assert len(result) == 1
    assert result[0]["label"] == "person"

# test 2 - nothing should pass through
def test_all_below():
    data = [
        {"label": "cat", "confidence": 0.30, "box": {}},
        {"label": "dog", "confidence": 0.45, "box": {}},
    ]
    result = filter_detections(data, 0.70)
    assert len(result) == 0

# test 3 - exactly at the threshold should be kept
def test_at_threshold():
    data = [
        {"label": "cat", "confidence": 0.70, "box": {}},
    ]
    result = filter_detections(data, 0.70)
    assert len(result) == 1

# test 4 - empty list should not crash
def test_empty():
    result = filter_detections([], 0.70)
    assert result == []


test_basic_filter()
test_all_below()
test_at_threshold()
test_empty()
print("all tests passed")