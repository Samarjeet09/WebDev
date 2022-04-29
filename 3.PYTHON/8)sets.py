# create an empty set
s = set()

# add elements
s.add(1)
s.add(4)
s.add(22)
s.add(222)
s.add(1)
# no element doesnt appear twice
print(s)
s.remove(4)

print(f"the set has {len(s)} elements ")