// week 3 javascript practice
// I already had the detection data from week 2
// wanted to see how to work with it in the browser

var detections = [
    { label: "person",  confidence: 0.91 },
    { label: "car",     confidence: 0.55 },
    { label: "bicycle", confidence: 0.72 },
    { label: "dog",     confidence: 0.40 }
]

// first thing I tried was just looping through and printing
for (var i = 0; i < detections.length; i++) {
    console.log(detections[i].label, detections[i].confidence)
}

// then I tried filtering, same logic as week 2 but in javascript
var filtered = []
for (var i = 0; i < detections.length; i++) {
    if (detections[i].confidence >= 0.70) {
        filtered.push(detections[i])
    }
}

console.log("above threshold:", filtered)

// this is the function connected to the button in basics.html
function showDetails() {
    var output = document.getElementById("output")

    var high = []
    for (var i = 0; i < detections.length; i++) {
        if (detections[i].confidence >= 0.70) {
            high.push(detections[i].label)
        }
    }

    output.textContent = "High confidence detections: " + high.join(", ")
}

// I also wanted to understand how fetch works before week 4
// this does not call a real api yet, just the structure
function getDetections(url) {
    fetch(url)
        .then(function(response) {
            return response.json()
        })
        .then(function(data) {
            console.log(data)
        })
        .catch(function(error) {
            console.log("something went wrong:", error)
        })
}