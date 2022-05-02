class point():
    # now we need to make a constructor
    # all the functions or methods that operate on objs  take first arguments as self whic represents
    # the object in Question
    # basically self refernces the obj we are dealing with
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = point(2, 9)
print(p.x)
print(p.y)
