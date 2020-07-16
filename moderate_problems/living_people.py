class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death


people = [Person(1901, 1910), Person(1910, 1947), Person(1905, 1919), Person(1907, 1988), Person(1902, 1975)]
min_year = 1900
max_year = 2000


def get_population_deltas(people, min_year, max_year):
    deltas = [0] * (max_year - min_year + 1)
    for person in people:
        deltas[person.birth - min_year] += 1
        deltas[person.death - min_year + 1] -= 1
    return deltas


def find_max_year(deltas):
    import sys
    max_val = -sys.maxsize
    currently_alive = 0
    for i in range(len(deltas)):
        currently_alive += deltas[i]
        if currently_alive > max_val:
            max_val = currently_alive
            year = i + min_year
    return year


population_deltas = get_population_deltas(people, min_year, max_year)
year = find_max_year(population_deltas)
print(year)
