# I wanted to understand how to work with a list of numbers in python
# starting simple - just finding the average of confidence scores

scores = [0.91, 0.76, 0.85, 0.60, 0.95]

total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print(average)

# that worked, so I turned it into a function so I can reuse it

def average_confidence(scores):
    if len(scores) == 0:
        return 0
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

print(average_confidence([0.91, 0.76, 0.85, 0.60, 0.95]))
print(average_confidence([]))