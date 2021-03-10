from faker import Faker
from random import randint
from dan_util import performance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonIterator:
    def __init__(self):
        self.registro = open("persons.csv", "r")
        self.actual_line = ""
        self._actual_person = None

    @staticmethod
    def make_person(**kwargs):
        name = kwargs['name'].strip()
        age = int(kwargs['age'])
        return Person(name, age)

    def __iter__(self):
        return self

    def __next__(self):
        self.actual_line = self.registro.readline()
        if self.actual_line == "name, age\n":
            self.actual_line = self.registro.readline()
        if not self.actual_line == "":
            name, age = self.actual_line.split(",")
            self.actual_person = self.make_person(name=name, age=age)
            return self.actual_person
        raise StopIteration


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


@performance
def printout():
    print([candidate.name for candidate in generate_classified_persons()])


#persons = PersonIterator()
#print([person for person in persons])

if __name__=="__main__":
    print("oi")
