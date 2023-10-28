import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_exists(self):
        self.assertAlmostEqual(self.stats.search('Semenko').team, "EDM")

    def test_search_doesnt_exists(self):
        self.assertIsNone(self.stats.search('Random'))

    def test_team(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    def test_top_assists(self):
        self.assertEqual(self.stats.top(3, SortBy.ASSISTS)[2].name, "Lemieux")

    def test_top_points(self):
        self.assertEqual(self.stats.top(3, SortBy.POINTS)[2].name, "Yzerman")

    def test_top_goals(self):
        self.assertEqual(self.stats.top(3, SortBy.GOALS)[2].name, "Kurri")

    def test_top_invalid(self):
        self.assertEqual(self.stats.top(3, None), [])
