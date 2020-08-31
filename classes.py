class Person():
    def __init__(self):
        self.name = "Hans"

class Glied(Person):
    def __init__(self):
        super().__init__()
        self.glied = "Bein"

    def print_glied(self):
        print(self.glied)

class Knorpel(Glied):
        
    def print_knorpel(self):
        print(self.glied)
        print(self.name)


knorp = Knorpel()
knorp.print_glied()
knorp.print_knorpel()
