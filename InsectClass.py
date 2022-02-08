import random

# bug stuff
class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.LoF = 0

    def get_Length(self):
        return self.LoF + random.randint(1, 10)
