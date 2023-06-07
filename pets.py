from ninja import Ninja
class Pet(Ninja):
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, health = 100, energy = 50):
        # I"m not sure how to get the SENSEI Bonus. You can't inherit an action and only use less than the inherited values
        # super().__init__(name, type)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        # self.max_health = health
        # self.max_energy = energy
    
    def sleep(self):
        # sleep = 25
        # self.energy = self.energy + sleep if self.energy + sleep <= self.max_energy else self.max_energy
        self.energy += 25
        self.energy = Pet.energy_check(self.energy, 25)
        return self

    def eat(self):
        self.energy = Pet.energy_check(self.energy, 5)
        self.health = Pet.health_check(self.health, 10)
        return self

    def play(self):
        self.health = Pet.health_check(self.health, 5)
        return self

    def noise(self):
        print(f'{self.name} the {self.type} screeches wildly!')
        return self

    @staticmethod
    def health_check(hp, amt):
        if hp + amt > 100:
            hp = 100
        else:
            hp = hp + amt
        return hp
    def energy_check(en, amt):
        if en + amt > 50:
            en = 50
        else:
            en + amt
        return en
