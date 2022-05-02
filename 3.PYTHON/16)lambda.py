people =[
    {"name": "sam","house": "p1house"},
    {"name": "samar","house": "p2house"},
    {"name": "pluto","house": "p3house"},
    {"name": "samarjeet","house": "p4house"},
]
 
# def f(person):
#     return person["name"]
# this is a very short one line expression so python gives us lambda ka option


# simply running people.sort will throw error

# people.sort(key=f)
people.sort(key= lambda person :person["name"])
print(people)