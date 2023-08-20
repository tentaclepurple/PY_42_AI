from mygame import Character
from mygame import Barbarian

conan = Barbarian("Joserra")
pepe = Barbarian("Pepe")

print(conan)

print(f"Joserra: {conan.life}. {conan.attval}. {conan. defval}")
print(f"Pepe: {pepe.life}. {pepe.attval}. {pepe. defval}")

conan.attack(pepe)