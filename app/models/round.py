from datetime import datetime
import managedb


class Round:
    """"""
    def __init__(self, name, matcheslist):
        """
        :param name:
        :param matcheslist:
        """
        self.name = name
        self.matches = matcheslist
        self.startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.endTime = ''
        self.rdb = managedb.TournamentDb()

    def enter_scores(self, results):
        """
        :param results:
        :return:
        """
        ii = 0
        for result in results:
            if result == "a":
                self.matches[ii][0][1] = 1
                self.matches[ii][1][1] = 0
            elif result == "b":
                self.matches[ii][0][1] = 0
                self.matches[ii][1][1] = 1
            else:
                self.matches[ii][0][1] = 0.5
                self.matches[ii][1][1] = 0.5
            ii += 1
        self.endTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def insert_round(self, tournament, index):
        """"""
        theround = tournament.tournees[index]
        thetournament = self.rdb.get_tournament_id(tournament)
        ser_round = {
            'id': index,
            'tournament': thetournament,
            'name': theround.name
        }
        cond1 = self.rdb.query.tournament == ''
        cond2 = self.rdb.query.count == index
        search1 = self.rdb.rounds.search(cond1 & cond2)
        if not search1:
            self.rdb.rounds.insert(ser_round)

    def init_match(self, tournament, indexr, indexm, p1, p2):

        thetournament = self.rdb.get_tournament_id(tournament)
        ser_match = {
            'id': indexm,
            'round': indexr,
            'tournament': thetournament,
            'player1': p1.firstName,
            'result1': 'TBD',
            'player2': p2.firstName,
            'result2:': 'TBD'
        }
        self.rdb.matches.insert(ser_match)
