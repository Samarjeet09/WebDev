# functional programming
# a way to modify the functions
# in py a function is a value like anyother
# we can pass then as inputs and outputs
# to other functions

def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("DONE")
    return wrapper

# we can add the decorator as


@announce
def hello():
    print("hello world")


hello()
