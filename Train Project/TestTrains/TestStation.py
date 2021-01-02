import unittest
from Station import Station
from Train import Train


class TestStation(unittest.TestCase):

    def setUp(self):
        self.station = Station()

    def test_add_travellers(self):
        self.station.traveller_count = 50
        travellers_to_add = 0
        self.station.add_travellers(travellers_to_add)
        self.assertEqual(50, self.station.traveller_count)

    def test_add_travellers_can_set_travellers(self):
        self.station.traveller_count = 50
        travellers_to_add = 5
        self.station.add_travellers(travellers_to_add)
        self.assertEqual(55, self.station.traveller_count)

    def test_add_travellers_negatives(self):
        travellers_to_add = -1
        self.assertRaises(Exception, self.station.add_travellers, travellers_to_add)

    def test_add_travellers_exceed_max_capacity(self):
        travellers_to_add = 201
        self.station.add_travellers(travellers_to_add)
        self.assertEqual(200, self.station.traveller_count)

    def test_arrivals(self):
        train = Train()
        self.station.train_arrive(train)
        self.assertIn(train, self.station.train_list)

    def test_train_arrive_travellers_board_new_arrival(self):
        train = Train()
        train.embark(30)
        self.station.add_travellers(60)
        self.station.travellers_board_new_arrival(20, train)
        self.assertEqual(40, self.station.traveller_count)
        self.assertEqual(50, train.passenger_count)

    def test_train_arrive_overflow_from_embark(self):
        train = Train()
        train.embark(30)
        self.station.add_travellers(100)
        self.station.travellers_board_new_arrival(80, train)
        self.assertEqual(55, self.station.traveller_count)
        self.assertEqual(75, train.passenger_count)


if __name__ == '__main__':
    unittest.main()
