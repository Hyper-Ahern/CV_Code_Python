from random import randint


def fill_station():
    station_travellers[0] += randint(0, 25)
    station_travellers[1] += randint(0, 25)
    station_travellers[2] += randint(0, 25)
    station_travellers[3] += randint(0, 25)
    station_travellers[4] += randint(0, 25)

    # If the station is full, no new people can be there
    if station_travellers[train_position] > 200:
        station_travellers[train_position] = 200

    return station_travellers[train_position]


def print_people():
    print(station_travellers[0])
    print(station_travellers[1])
    print(station_travellers[2])
    print(station_travellers[3])
    print(station_travellers[4])


def disembark():
    people_dis = train
    disembarked_people = 0
    for x in range(0, people_dis):
        random_dis = randint(0, 9)
        if random_dis < 4:
            disembarked_people = disembarked_people + 1
    return disembarked_people


def embark():
    people = station_travellers[train_position]
    embarking_people = 0
    for x in range(0, people):
        random = randint(0, 1)
        if random == 1:
            embarking_people = embarking_people + 1
    return embarking_people


# MAIN ---------------

train = 0
station_travellers = [0, 0, 0, 0, 0]
train_position = 0
number_of_circuits = 10

while number_of_circuits > 0:
    train_position = 0
    while train_position <= 4:
        fill_station()

        # 50% chance of passengers embarking done through a random number generator
        embarking = embark()

        # People disembarking have a 40% chance to get off the train
        disembarking = disembark()

        # People simply getting off the train and leaving the station
        train = train - disembarking

        # If the train is not full, do the following
        if train < 75:
            remainingSeats = 75 - train
            if embarking < remainingSeats:
                # add to train and subtract from station
                train = train + embarking
                station_travellers[train_position] = station_travellers[train_position] - embarking
            else:
                embarking = embarking - remainingSeats
                # we already know the train will be full
                train = 75
                station_travellers[train_position] = station_travellers[train_position] - embarking
        train_position = train_position + 1
    number_of_circuits -= 1

print_people()
train = 0
train_position = 0



