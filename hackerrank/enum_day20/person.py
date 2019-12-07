import enum


class Person:
    class HairColor(enum.Enum):
        BLOND = 1
        BROWN = 2
        BLACK = 3
        PINK = 4
        OTHER = 0

    hair_color = HairColor(1)


person = Person()
print(person.hair_color)
print(person.hair_color.BLACK)

peter_parker = Person()
spider_man = peter_parker

print(peter_parker.hair_color)
print(spider_man.hair_color)

peter_parker.hair_color = Person.HairColor.PINK
print(peter_parker.hair_color)
print(spider_man.hair_color)
