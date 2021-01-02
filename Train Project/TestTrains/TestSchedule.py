import unittest
from Schedule import Schedule
from Station import Station


class TestSchedule(unittest.TestCase):

    def setUp(self):
        self.schedule = Schedule()

    def test_schedule_add_station(self):
        station = Station()
        self.schedule.add_station(station)
        self.assertIn(station, self.schedule.station_list)

    def test_schedule_add_station_incrementing_stations(self):
        station = Station()
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)

    def test_schedule_add_station_multiple_incrementing_stations(self):
        station = Station()
        station2 = Station()
        station3 = Station()
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)
        self.schedule.add_station(station2)
        self.assertEqual(3, self.schedule.amount_of_stations)
        self.schedule.add_station(station3)
        self.assertEqual(4, self.schedule.amount_of_stations)

    def test_schedule_add_station_multiple_incrementing_stations_with_starting_station(self):
        station = Station()
        station2 = Station()
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)
        self.schedule.add_station(station2)
        self.assertEqual(3, self.schedule.amount_of_stations)
        self.schedule.add_station(station)
        self.assertEqual(3, self.schedule.amount_of_stations)

    def test_schedule_add_station_multiple_incrementing_stations_all_starting_stations(self):
        station = Station()
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)
        self.schedule.add_station(station)
        self.assertEqual(1, self.schedule.amount_of_stations)

    # starting with the assumption that it is ok to add a final station to the list to ensure the first and last are
    # the same even if the user didn't specify this. Another possible design would be to throw an error if the user
    # didn't specify the last stop to be the same as the first.
    def test_schedule_first_last_same_stop_single_station(self):
        station = Station()
        self.schedule.add_station(station)
        station1 = self.schedule.station_list[0]
        station2 = self.schedule.station_list[self.schedule.amount_of_stations - 1]
        self.assertEqual(station1, station2)

    def test_schedule_first_last_same_stop_two_stations(self):
        station1 = Station()
        station2 = Station()
        self.schedule.add_station(station1)
        self.schedule.add_station(station2)
        station_one_test = self.schedule.station_list[0]
        station_two_test = self.schedule.station_list[self.schedule.amount_of_stations - 1]
        self.assertEqual(station_one_test, station_two_test)

    # discuss how I could have caught the edge case that I am continuously adding stations that the user
    # did not intend (first design was to just append the first station to the end but this would make the schedule
    # contain many unintended stops to the first station) *EDIT* adding a count check at the end prevents this I think!
    def test_schedule_first_last_same_stop_multiple_stations(self):
        station1 = Station()
        station2 = Station()
        station3 = Station()
        self.schedule.add_station(station1)
        self.schedule.add_station(station2)
        station_one_test = self.schedule.station_list[0]
        station_two_test = self.schedule.station_list[self.schedule.amount_of_stations - 1]
        self.assertEqual(station_one_test, station_two_test)
        self.schedule.add_station(station3)
        station_one_test = self.schedule.station_list[0]
        station_two_test = self.schedule.station_list[self.schedule.amount_of_stations - 1]
        self.assertEqual(station_one_test, station_two_test)
        self.assertEqual(4, self.schedule.amount_of_stations)