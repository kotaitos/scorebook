from typing import List, Optional
from datetime import datetime

class Scorebook:
  def __init__(self,
               home_team: str = 'Home Team',
               away_team: str = 'Away Team',
               datetime: datetime = datetime.now(),
               start_datetime: Optional[datetime] = None,
               end_datetime: Optional[datetime] = None,
               stadium: Optional[str] = None,
               stadium_condition: Optional[str] = None,
               weather: Optional[str] = None,
               audience: Optional[str] = None,
               home_score: int = 0,
               away_score: int = 0,
               innings: int = 9,
               inning_results: List = []):
    self.datetime = datetime
    self.start_datetime = start_datetime
    self.end_datetime = end_datetime
    self.home_team = home_team
    self.away_team = away_team
    self.home_score = home_score
    self.away_score = away_score
    self.innings = innings
    self.stadium = stadium
    self.inning_results = inning_results
    self.stadium_condition = stadium_condition
    self.weather = weather
    self.audience = audience
    