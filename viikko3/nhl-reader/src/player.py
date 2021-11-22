import datetime
import requests

class Player:
    def __init__(self, name, nationality, assists, goals, team,  assists_and_goals):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.assists_and_goals = assists_and_goals
    
    def __str__(self):
        return f"{self.name:20} {self.team:2} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals + self.assists):2}"

class PlayerReader():
    def __init__(self):
        self.players = []
        self.get_players()
    
    def get_players(self):
        url = "https://nhlstatisticsforohtu.herokuapp.com/players"
        response = requests.get(url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['team'],
                player_dict["goals"] + player_dict["assists"]
            )
            self.players.append(player)

class PlayerStats(PlayerReader):
    def __init__(self, players):
        super().__init__()

    def top_scorers_by_nationality(self, nationality):
        result = []
        for player in self.players:
            if player.nationality == nationality:
                result.append(player)

        result.sort(reverse = True, key = lambda x: x.assists_and_goals)

        return result





