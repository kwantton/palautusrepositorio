from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader

def main():
    haettava_url = 'https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt'    # injektiota varten
    player_reader = PlayerReader(haettava_url)                                      # injektiota varten
    stats = StatisticsService(player_reader)                                        # injektio
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("\nTop point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("\nTop goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("\nTop by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)

if __name__ == "__main__":
    main()