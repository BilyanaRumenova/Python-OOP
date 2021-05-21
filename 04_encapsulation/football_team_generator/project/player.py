class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        return f"Player: {self.__name}\nEndurance: {self.__endurance}\nSprint: {self.__sprint}\n" \
               f"Dribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}\n"



# import unittest
#
# from encapsulation_LAB.football_team_generator.project.team import Team
#
# class Tests(unittest.TestCase):
#     def test_player_init(self):
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         self.assertEqual(p.name, "Pall")
#         self.assertEqual(p.endurance, 3)
#         self.assertEqual(p.sprint, 3)
#         self.assertEqual(p.passing, 3)
#         self.assertEqual(p.dribble, 3)
#         self.assertEqual(p.shooting, 3)
#
#     def test_player_str(self):
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         result = str(p)
#         expected = "Player: Pall\nEndurance: 3\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3\n"
#         self.assertEqual(expected, result)
#
#     def test_team_init(self):
#         t = Team("Best", 10)
#         self.assertEqual(t.name, "Best")
#         self.assertEqual(t.rating, 10)
#         self.assertEqual(len(t.players), 0)
#
#     def test_team_add_successful(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#
#         self.assertEqual(t.add_player(p), "Player Pall joined team Best")
#
#     def test_team_add_fail(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#
#         t.add_player(p)
#         self.assertEqual(t.add_player(p), "Player Pall has already joined")
#
#     def test_team_remove_successful(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         t.add_player(p)
#         exp = t.remove_player("Pall")
#         self.assertEqual(exp, p)
#
#     def test_team_remove_fail(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         result = "Player Pall not found"
#         exp = t.remove_player("Pall")
#         self.assertEqual(exp, result)
#
#
# if __name__ == "__main__":
#     unittest.main()
#

