from unittest import TestCase
from route import Route
from station import Station


class TestRoute(TestCase):
    def setUp(self):
        self.terminal = Station()
        self.middle_station = Station()
        self.valid_route = Route([self.terminal, self.middle_station, self.terminal])

    def test_creation_allows_base_case(self):
        try:
            terminal = Station()
            Route([terminal, Station(), terminal])
        except ValueError:
            self.fail("Raised exception with legal constructor arguments")

    def test_creation_fails_when_first_and_last_station_are_different(self):
        self.assertRaises(ValueError, Route, [Station(), Station()])

    def test_creation_fails_if_consecutive_stations_are_identical(self):
        fail_station = Station()
        self.assertRaises(ValueError, Route, [fail_station, fail_station])

    def test_go_to_next_station_base_case(self):
        self.assertTrue(self.valid_route.go_to_next_station())
        self.assertEqual(self.middle_station, self.valid_route.current_station)

    def test_go_to_next_station_fails_when_at_final_station(self):
        self.assertTrue(self.valid_route.go_to_next_station())
        self.assertTrue(self.valid_route.go_to_next_station())
        self.assertFalse(self.valid_route.go_to_next_station())
