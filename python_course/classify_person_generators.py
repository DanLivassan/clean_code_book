from faker import Faker
from random import randint
from dan_util import performance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def can_enlist_filter(max_age: int):
    def can_enlist_for_army(person: Person) -> bool:
        return person.age <= max_age
    return can_enlist_for_army


def generate_dummy_persons_csv(numbers_of_persons: int):
    fake = Faker()
    with open("persons.csv", 'w+') as file:
        file.write("name, age\n")
        for i in range(numbers_of_persons):
            person = Person(fake.name(), randint(29, 45))
            file.write(f"{person.name}, {person.age}\n")


def generate_persons_by_csv_without_generator():
    with open("persons.csv", "r") as file:
        persons = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            name, age = line.split(',')
            name = name.strip()
            age = int(age.strip())
            persons.append(Person(name, age))
        return persons


def generate_persons_by_csv_with_generator():
    with open("persons.csv", "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            name, age = line.split(',')
            name = name.strip()
            age = int(age.strip())
            yield Person(name, age)


#generate_dummy_persons_csv(1000000)


def generate_classified_persons():
    persons = generate_persons_by_csv_with_generator()
    my_filter = can_enlist_filter(30)
    candidates = filter(my_filter, persons)
    return candidates


@performance
def printout():
    print([candidate.name for candidate in generate_classified_persons()])


printout()