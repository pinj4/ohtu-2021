
import datetime
from player import Player, PlayerReader, PlayerStats

def main():
    #url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
