class Route:
    def __init__(self, station_list):
        self._current_station_index = 0
        self._station_list = station_list

        last_station = len(station_list) - 1
        if station_list[0] != station_list[last_station]:
            raise ValueError("Route is not a circuit")

        for i in range(last_station):
            if station_list[i] == station_list[i + 1]:
                raise ValueError("Route cannot visit same station twice in a row")

    def go_to_next_station(self):
        if self._current_station_index < len(self._station_list) - 1:
            self._current_station_index += 1
            return True
        else:
            return False

    @property
    def current_station(self):
        return self._station_list[self._current_station_index]
