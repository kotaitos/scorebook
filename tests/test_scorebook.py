import unittest
from datetime import datetime
from scorebook.scorebook import Scorebook

class TestScorebook(unittest.TestCase):
  def test_init_default(self):
    scorebook = Scorebook()
    self.assertEqual(scorebook.home_team, 'Home Team')
    self.assertEqual(scorebook.away_team, 'Away Team')
    self.assertEqual(scorebook.datetime.date(), datetime.now().date())
    self.assertEqual(scorebook.start_datetime, None)
    self.assertEqual(scorebook.end_datetime, None)
    self.assertEqual(scorebook.stadium, None)
    self.assertEqual(scorebook.stadium_condition, None)
    self.assertEqual(scorebook.weather, None)
    self.assertEqual(scorebook.audience, None)
    self.assertEqual(scorebook.home_score, 0)
    self.assertEqual(scorebook.away_score, 0)
    self.assertEqual(scorebook.innings, 9)
    self.assertEqual(scorebook.inning_results, [])
    

if __name__ == '__main__':
  unittest.main()
  