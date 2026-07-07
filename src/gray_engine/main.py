"""
Gray Capital Football Prediction Engine
Main entry point
"""

from .ratings import TeamRatings



def main():
    print("=" * 50)
    print("GRAY CAPITAL FOOTBALL PREDICTION ENGINE")
    print("=" * 50)
    print()

    ratings = TeamRatings()
    best_team = ""
    best_rating = 0

    for team, info in ratings.teams.items():
        print(team, info["rating"])

        if info["rating"] > best_rating:
            best_rating = info["rating"]
            best_team = team

    print()
    print("Highest Rated Team:")
    print(best_team, best_rating)

    print()
    print("Engine initialized successfully.")
    print(f"Current teams loaded: {len(ratings.teams)}")


if __name__ == "__main__":
    main()
