import random

first = [
    "joe",
    "steve",
    "john",
]

last = [
    "jones",
    "smith",
    "johanson",
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)