from random import randint


class Station:

    def __init__(self):
        self.traveller_count = 0
        self.MAX_CAPACITY = 200
        self.train_list = []

    def add_travellers(self, travellers):
        if travellers < 0:
            raise Exception
        self.traveller_count += travellers
        if self.traveller_count > self.MAX_CAPACITY:
            self.traveller_count = self.MAX_CAPACITY

    def spawn_travellers(self):
        spawned_people = randint(0,25)
        self.add_travellers(spawned_people)

    def train_arrive(self, train):
        self.train_list.append(train)
        train.passengers_depart_on_arrival()
        self.travellers_board_new_arrival(self.get_random_travellers(), train)

    def travellers_board_new_arrival(self, number_of_people, train):
        overflow = train.embark(number_of_people)
        self.traveller_count -= number_of_people - overflow

    def get_random_travellers(self):
        embarked_people = 0
        for x in range(0, self.traveller_count):
            random_number = randint(0, 9)
            if random_number < 5:
                embarked_people += 1
        return embarked_people
