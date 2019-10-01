import random

first = [
    "joe",
    "steve"
]

last = [
    "jones",
    "smith"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)