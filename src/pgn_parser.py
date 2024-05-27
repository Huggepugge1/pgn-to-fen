import pgn


class PGN_Parser:
    def __init__(self, string):
        self.string = string
        
        self.event = None
        self.site = None
        self.date = None
        self.round = None
        self.white = None
        self.black = None
        self.result = None
        self.UTCDate = None
        self.UTCTime = None
        self.WhiteRatingDiff = None
        self.BlackRatingDiff = None
        self.WhiteTitle = None
        self.BlackTitle = None
        self.ECO = None
        self.Opening = None
        self.TimeControl = None
        self.Termination = None

    def parse(self):
        for line in self.string.split("\n"):
            if line[0] == "[":
                line = line[1:-1].split("\"")
                match line[0][:-1]:
                    case "Event":
                        self.event = line[1]
                    case "Site":
                        self.site = line[1]
                    case "Date":
                        self.date = line[1]
                    case "Round":
                        self.round = line[1]
                    case "White":
                        self.white = line[1]
                    case "Black":
                        self.black = line[1]
                    case "Result":
                        self.result = line[1]
                    case "UTCDate":
                        self.UTCDate = line[1]
                    case "UTCTime":
                        self.UTCTime = line[1]
                    case "WhiteRatingDiff":
                        self.WhiteRatingDiff = line[1]
                    case "BlackRatingDiff":
                        self.BlackRatingDiff = line[1]
                    case "WhiteTitle":
                        self.WhiteTitle = line[1]
                    case "BlackTitle":
                        self.BlackTitle = line[1]
                    case "ECO":
                        self.ECO = line[1]
                    case "Opening":
                        self.Opening = line[1]
                    case "TimeControl":
                        self.TimeControl = line[1]
                    case "Termination":
                        self.Termination = line[1]

        return pgn.PGN(
            self.event,
            self.site,
            self.date,
            self.round,
            self.white,
            self.black,
            self.result,
            self.UTCDate,
            self.UTCTime,
            self.WhiteRatingDiff,
            self.BlackRatingDiff,
            self.WhiteTitle,
            self.BlackTitle,
            self.ECO,
            self.Opening,
            self.TimeControl,
            self.Termination
        )

