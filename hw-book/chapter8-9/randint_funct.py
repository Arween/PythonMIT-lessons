# x = randint(1, 6)

class Die():
    def __init__(self, sides=6, throws=10):

        self.sides = sides
        self.throws = throws

    def roll_die(self):

        # for x in range(1, self.throws)
        x = randint(1, self.sides)
        print ('Throws: ' +  str(x))
        print (str(self.throws))


six = Die(6, 10)
six.roll_die()