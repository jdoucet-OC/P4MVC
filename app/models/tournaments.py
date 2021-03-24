import managedb


class Tournament:
    """"""
    def __init__(self, name, place, date,
                 timetype, desc):
        self.name = name
        self.place = place
        self.date = date
        self.turns = 4
        self.tournees = []
        self.players = []
        self.timeType = timetype
        self.description = desc
        self.tdb = managedb.TournamentDb()

    def insert_tournament(self):
        """
        :return:
        """
        index = self.tdb.tournament.__len__()
        ser_tournament = {
            'id': index,
            'name': self.name.lower(),
            'place': self.place.lower(),
            'date': self.date,
            'turns': self.turns,
            'timeType': self.timeType,
            'description': self.description

        }

        cond1 = self.tdb.query.name == self.name.lower()
        cond2 = self.tdb.query.place == self.place.lower()
        cond3 = self.tdb.query.date == self.date

        search1 = self.tdb.tournament.search(cond1 & cond2 & cond3)

        if not search1:
            self.tdb.tournament.insert(ser_tournament)

    def sort_by_score(self):
        """
        :return:
        """
        scoreboard = []
        for player in self.players:
            pscore = [player, 0]
            for turn in self.tournees:
                for match in turn.matches:
                    if player in match[0]:
                        pscore[1] += match[0][1]
                    if player in match[1]:
                        pscore[1] += match[1][1]
            scoreboard.append(pscore)
        sortedscoreboard = sorted(scoreboard, key=lambda score: score[1], reverse=True)

        return sortedscoreboard

    def sort_by_elo(self):
        """
        :return:
        """
        sortedlist = sorted(self.players, key=lambda elosort: elosort.elo)
        return sortedlist
