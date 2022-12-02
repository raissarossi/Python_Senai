class Animal:
    def __init__(self, name='', species='', weight= 0):
        self.name = name
        self.species = species
        self.weight = weight
        self.genere = ''

    def hunt(self):
        if self.weight <= 10:
            print(f'{self.name} running away')
        else:
            print(f"{self.name} on the hunt")

    def define_genere(self):
        if self.name.endswith('a'):
            self.genere = 'F'
        else:
            self.genere = 'M'