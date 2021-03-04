list = [
    {"name": "Danilo", "age": 31},
    {"name": "Pedro", "age": 17},
    {"name": "Paulo", "age": 30},
    {"name": "Fagner", "age": 20}
]


def filter_list(list, age):
    """
    Example of bad naming
    :param list:
    :param age:
    :return:
    """
    d = []
    for i, val in enumerate(list):
        if val["age"] >= age:
            d.append(val)
    return d


def filter_persons_by_min_age(persons: [dict], min_age: int) -> [dict]:
    """
    :param persons:
    :param min_age:
    :return:
    """
    filtered_person = []
    for person in persons:
        if person["age"] >= min_age:
            filtered_person.append(person)
    return filtered_person


print(filter_list(list, 18) == filter_persons_by_min_age(list, 18))
