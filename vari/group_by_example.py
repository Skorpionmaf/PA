import itertools

def get_state(city_state):
    return city_state[1]

city_state_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'), ('Anchorage', 'AK'), ('Nome', 'AK'),('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')]

groups = []
uniquekeys = []

for k, g in itertools.groupby(city_state_list, get_state):
    groups.append(list(g))
    uniquekeys.append(k)

print(groups)
print(uniquekeys)

d = { x[0][1] : [t[0] for t in x] for x in groups}
print(d)