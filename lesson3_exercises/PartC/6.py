scores = [80, 65, 90, 55, 70, 45]

passes = 0
failures = 0

for score in scores:
    if score >= 70:
        passes += 1
    else:
        failures += 1

print("Passes:", passes)
print("Failures:", failures)