from random import randint


class Train:

    def __init__(self):
        self.passenger_count = 0

    def embark(self, passengers):
        if passengers < 0:
            raise Exception
        self.passenger_count += passengers
        if self.passenger_count > 75:
            overflow = self.passenger_count - 75
            self.passenger_count = 75
            return overflow
        else:
            return 0

    def disembark(self, people_disembarking):

        if people_disembarking > self.passenger_count:
            raise Exception
        if people_disembarking < 0:
            raise Exception
        self.passenger_count -= people_disembarking

    def passengers_depart_on_arrival(self):
        disembarked_people = 0
        for x in range(0, self.passenger_count):
            random_number = randint(0, 9)
            if random_number < 4:
                disembarked_people += 1
        self.disembark(disembarked_people)





