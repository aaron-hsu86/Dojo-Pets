class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print(f'{self.first_name} {self.last_name} walks their pet {self.pet.name}')
        return self

    def feed(self):
        print(f'{self.first_name} {self.last_name} gives {self.pet.name} a {self.pet_food}')
        self.pet.eat()
        print(f'{self.pet.name} chews on {self.pet_food}')
        return self

    def bathe(self):
        print(f'{self.first_name} {self.last_name} attempts to give {self.pet.name} a bath.')
        self.pet.noise()
        return self