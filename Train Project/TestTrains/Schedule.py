class Schedule:

    def __init__(self):
        self.station_list = []
        self.amount_of_stations = 0

    # Ensures that the start and stop stations are the same and allows the user to make a schedule of their choosing
    # Also removes duplicates because the train cannot go from station A to station A
    def add_station(self, station):
        self.amount_of_stations += 1
        self.station_list.append(station)

        # if the passed in station is not the starting point
        if station != self.station_list[0]:

            # if the number of stations exceeds 2 since I am appending the passed in station before the checks
            if self.amount_of_stations > 2:
                if self.station_list[0] == self.station_list[self.amount_of_stations - 2]:
                    self.station_list.remove(self.station_list[self.amount_of_stations - 2])
                    self.amount_of_stations -= 1

        # if the last and first station aren't the same, make them the same by adding the first station to the end
        if self.station_list[0] != self.station_list[self.amount_of_stations - 1]:
            self.station_list.append(self.station_list[0])
            self.amount_of_stations += 1

        # if the station is passed consecutive duplicates, take one of them off the list
        if self.amount_of_stations >= 2:
            if self.station_list[self.amount_of_stations - 1] == self.station_list[self.amount_of_stations - 2]:
                self.station_list.remove(self.station_list[self.amount_of_stations - 2])
                self.amount_of_stations -= 1
