class Flight():
    def __init__(self, capacity):
        self.cap = capacity
        self.passengers = []

    def add(self, name):
        # if self.open_seats() ==0: this is the normal way
        # now the python way
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.cap - len(self.passengers)


flight = Flight(3)
people = ["p1", "p2", "p3", "p4"]

for i in people:
    ssucess = flight.add(i)
    if ssucess:
        print(f"Added {i} to the flight")
    else:
        print(f"N0 available seats for {i}")
