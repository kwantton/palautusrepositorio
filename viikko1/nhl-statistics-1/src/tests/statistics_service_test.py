import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [                                # a list of players, just like in the actual Player_reader().get_players()
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_get_players(self):
        self.assertEqual(self.stats._players, [
        Player("Semenko", "EDM", 4, 12),    # 16
        Player("Lemieux", "PIT", 45, 54),   # 99
        Player("Kurri",   "EDM", 37, 53),   # 90
        Player("Yzerman", "DET", 42, 56),   # 98
        Player("Gretzky", "EDM", 35, 89)    # 124
        ])
    
    def test_search_players_finds_target(self):
        self.assertEqual(self.stats.search('Kurri'), Player('Kurri', 'EDM', 37, 53))
    
    def test_search_players_does_not_find_target(self):
        self.assertEqual(self.stats.search('Kuraweogijawori'), None)
    
    def test_team_positive(self):
        self.assertEqual(self.stats.team('EDM'), [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
            ])
    
    def test_team_negative(self):
        self.assertEqual(self.stats.team('Kuraweogijawori'), [])

    def test_top_1(self):
        self.assertEqual(self.stats.top(0), [
            Player("Gretzky", "EDM", 35, 89),   # 124
            # Player("Lemieux", "PIT", 45, 54),   # 99
            # Player("Yzerman", "DET", 42, 56)    # 98
        ])
    
    def test_top_3(self):
        self.assertEqual(self.stats.top(2), [
            Player("Gretzky", "EDM", 35, 89),   # 124
            Player("Lemieux", "PIT", 45, 54),   # 99
            Player("Yzerman", "DET", 42, 56)    # 98
        ])
    
    def test_top_negative(self):
        self.assertEqual(self.stats.top(-3), [])
    
    def test_top_goals(self):
        self.assertEqual(self.stats.top(2, SortBy.GOALS), [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53)
        ])
    
    def test_top_assists(self):
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS), [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54)
        ])
    
    def test_invalid_sort_raises_value_error(self):
        # attempt to call top with an invalid sort criterion: asked ChatGPT how to do this, cool!
        with self.assertRaises(ValueError) as context:
            self.stats.top(5, sort_by_what="INVALID_SORT_CRITERION")
        
        self.assertEqual(str(context.exception), "magic number should be 1, 2 or 3")