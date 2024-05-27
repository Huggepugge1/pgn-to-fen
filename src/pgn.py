class PGN:
    def __init__(
            self,
            event,
            site,
            date,
            round,
            white,
            black,
            result,
            UTCDate,
            UTCTime,
            WhiteRatingDiff,
            BlackRatingDiff,
            WhiteTitle,
            BlackTitle,
            ECO,
            Opening,
            TimeControl,
            Termination
        ):

        self.event = event
        self.site = site
        self.date = date
        self.round = round
        self.white = white
        self.black = black
        self.result = result
        self.UTCDate = UTCDate
        self.UTCTime = UTCTime
        self.WhiteRatingDiff = WhiteRatingDiff
        self.BlackRatingDiff = BlackRatingDiff
        self.WhiteTitle = WhiteTitle
        self.BlackTitle = BlackTitle
        self.ECO = ECO
        self.Opening = Opening
        self.TimeControl = TimeControl
        self.Termination = Termination
        
