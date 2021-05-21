from unittest import TestCase, main

from project.appliances.appliance import Appliance
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    name = 'Konst'
    budget = 800
    members_count = 2

    def setUp(self):
        self.room = Room(self.name, self.budget, self.members_count)

    def test_attributes_are_set(self):
        self.assertEqual(self.name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members_count, self.room.members_count)
        self.assertListEqual([], self.room.children)
        for attr in ["family_name", "budget", "members_count", "expenses", "children"]:
            self.assertTrue(hasattr(self.room, attr))

    def test_expenses__set_positive_value(self):
        self.room.expenses = 50.00
        self.assertEqual(50, self.room.expenses)

    def test_expenses__set_0_value(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_expenses__cannot_set_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -50.00
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses_when_0_consumers(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when_1_consumer(self):
        child = [Child(10, 5, 6)]
        self.room.calculate_expenses(child)

        self.assertEqual(child[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses_when_more_consumers(self):
        children = [Child(10, 5, 6), Child(5, 5, 5)]
        appliances = [Appliance(15)]
        self.room.calculate_expenses(children, appliances)

        expected = children[0].get_monthly_expense() + children[1].get_monthly_expense() + appliances[0].get_monthly_expense()

        self.assertEqual(expected, self.room.expenses)


if __name__ == '__main__':
    main()
