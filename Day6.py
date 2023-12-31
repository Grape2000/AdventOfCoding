# Wait For It - Boat race
# time allowed for each race + best distance ever recorded
# go farther in each race then current record holder
# start: 0 mm per millisecond


# given: list of times and distance
# want: (3) product of number of ways we can beat all records
# how to (1) beat the record for (2) all races


# read inmput
def read_input(handle):
    time = []
    dist = []
    with open(handle, "r") as races:
        for line in races.readlines():
            split = line.replace("\s+", " ").split()[1:]
            if line.startswith("Time"):
                time = [int(x) for x in split]
            else:
                dist = [int(x) for x in split]
    return time, dist



# (1) beat records

# type in terminal: 

def beat_race(total_time, record_distance):
    winning_strategies = 0
    distances = []
    for button_press in range(total_time+1):
        v = button_press
        travel_time = total_time - button_press
        dist = v * travel_time
        distances.append(dist)
        if dist > record_distance:
            winning_strategies += 1
    return distances, winning_strategies


# (2) multiplication of number of ways: w1 * w2 * ... * Wn
def product(array):
    result = 1
    for num in array:
        result *= num
    return result


# winning combinations
times, records = read_input("Day6.txt")
winning_combinations = []
for t, record in zip(times, records):
    _, w = beat_race(t, record)
    winning_combinations.append(w)

product(winning_combinations)



##########################


race_time_input = []
records_input = []

input = open("Day6.txt", "r")
for line in input.readlines():
    line = line.strip("\n")
    if line.startswith("Time"):
        race_time_input.append(line)
    else:
        records_input.append(line)

race_time_input = race_time_input[0]
race_time_input = race_time_input.split(":")
race_time_input = race_time_input[1]
race_time_input = race_time_input.split(" ")
race_time_input = [item for item in race_time_input if item != '']

records_input = records_input[0]
records_input = records_input.split(":")
records_input = records_input[1]
records_input = records_input.split(" ")
records_input = [item for item in records_input if item != '']

#print(race_time_input, records_input)

race_times_records_dict = {}
for items in range(len(race_time_input)):
    race_times_records_dict[int(race_time_input[items])] = int(records_input[items])
#print(race_times_records_dict)

ways = []

for race_time, record in race_times_records_dict.items():
    #print(record)
    #print(race_time)
    distances = []
    for bpt in range(race_time):
        distance = bpt * (race_time - bpt)
        if distance > record:
            distances.append(distance)
        #print(distances)
        number_of_ways = 0
        for way in distances:
            number_of_ways = number_of_ways + 1
            #print(number_of_ways)
    ways.append(number_of_ways)
#print(ways)

product = 1
for numbers in ways:
    product = product * numbers

print(product)