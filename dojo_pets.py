from ninja import Ninja
from pets import Pet



Monkey = Pet('Jackie', 'monkey', 'stealing')

Jack = Ninja('Jack', 'Sparrow', 'rum', 'biscuits', Monkey)

# checking health and energy dont go above max, since all actions add energy, not take any away
# Monkey.sleep().eat().play().noise()
# print(f'monkey health: {Monkey.health}')
# print(f'monkey energy: {Monkey.energy}')

Jack.walk().feed().bathe()