import random

def random_num():
    return random.randint(0, 10)

first = [
    "joe",
    "steve",
    "john",
    "adam",
    "alex",
    "andrea",
    "amy",
    "jane",
    "amy",
    "sarah",
    "sam",
    "smitty",
    "sydney",
    "cameron",
    "benny",
    "bobert",
    "bonnie",
    "belle",
    "kate",
    "michael",
    "tommy",
    "henry"
]

last = [
    "jones",
    "smith",
    "johanson",
    "abner",
    "abbey",
    "aber",
    "jawannaman",
    "solo",
    "sanders",
    "sinker",
    "sawdust",
    "diaz",
    "beck",
    "bender",
    "boxer",
    "boozer",
    "plus8",
    "jozner",
    "kilma",
    "dougles"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)
print(random_num())