import pgn_parser

PGN = pgn_parser.PGN_Parser(
    """[Event \"Rated Bullet tournament https://lichess.org/tournament/yc1WW2Ox\"]
[Site \"https://lichess.org/PpwPOZMq\"]
[Date \"2017.04.01\"]
[Round \"-\"]
[White \"Abbot\"]
[Black \"Costello\"]
[Result \"0-1\"]
[UTCDate \"2017.04.01\"]
[UTCTime \"11:32:01\"]
[WhiteElo \"2100\"]
[BlackElo \"2000\"]
[WhiteRatingDiff \"-4\"]
[BlackRatingDiff \"+1\"]
[WhiteTitle \"FM\"]
[ECO \"B30\"]
[Opening \"Sicilian Defense: Old Sicilian\"]
[TimeControl \"300+0\"]
[Termination \"Time forfeit\"]""").parse()

print(vars(PGN))
