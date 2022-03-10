import sys
import json

data = list(map(str, sys.stdin))

with open('scoring.json') as f:
    data2 = json.load(f)

r = 0
for i in range(len(data)):
    if data[i] == "ok\n":
        j = 0
        while i + 1 not in data2["scoring"][j]["required_tests"]:
            j = j + 1
        r = r + data2["scoring"][j]["points"] / len(data2["scoring"][j]["required_tests"])
print(r)
