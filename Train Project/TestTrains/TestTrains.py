import unittest
from Train import Train


class TestTrain(unittest.TestCase):

    def setUp(self):
        self.train1 = Train()

    def test_embark_set_zero(self):
        self.train1.embark(0)
        self.assertEqual(0, self.train1.passenger_count)

    def test_embark_can_set_passenger(self):
        passengers = 5
        self.train1.embark(passengers)
        self.assertEqual(passengers, self.train1.passenger_count)

    def test_embark_add_passengers(self):
        passengers = 1
        self.train1.embark(passengers)
        passengers = 5
        self.train1.embark(passengers)
        self.assertEqual(6, self.train1.passenger_count)

    def test_embark_overflow_when_exceeds_capacity(self):
        passengers = 76
        overflow = self.train1.embark(passengers)
        self.assertLessEqual(self.train1.passenger_count, 75)
        self.assertLessEqual(1, overflow)

    def test_embark_return_overflow(self):
        passengers = 5
        overflow = self.train1.embark(passengers)
        self.assertEqual(0, overflow)

    def test_embark_negative_passengers(self):
        passengers = -1
        self.assertRaises(Exception, self.train1.embark, passengers)

    def test_disembark_set_zero(self):
        self.train1.embark(50)
        people_disembarking = 0
        self.train1.disembark(people_disembarking)
        self.assertEqual(50, self.train1.passenger_count)

    def test_disembark_can_set_passengers(self):
        self.train1.embark(50)
        people_disembarking = 5
        self.train1.disembark(people_disembarking)
        self.assertEqual(45, self.train1.passenger_count)

    def test_disembark_subtract_passengers(self):
        self.train1.embark(50)
        people_disembarking = 1
        self.train1.disembark(people_disembarking)
        people_disembarking = 5
        self.train1.disembark(people_disembarking)
        self.assertEqual(44, self.train1.passenger_count)

    def test_disembark_remove_too_many_passengers(self):
        self.train1.embark(50)
        people_disembarking = 76
        self.assertRaises(Exception, self.train1.disembark, people_disembarking)

    def test_disembark_negative_passengers(self):
        people_disembarking = -1
        self.assertRaises(Exception, self.train1.disembark, people_disembarking)
