from ..models import managedb


class Tournament:
    """"""
    def __init__(self, name, place, date,
                 timetype, desc):
        """
        :param name: tournament name
        :param place: tournament location
        :param date: tournament date (dd/mm/yyyy)
        :param timetype: tournament chess time type
        :param desc: tournament description
        """
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
        :return: insert tournament in DB
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

        for tours in self.tdb.tournament.all():
            cond1 = tours['name'] == self.name.lower()
            cond2 = tours['place'] == self.place.lower()
            cond3 = tours['date'] == self.date
            if cond1 and cond2 and cond3:
                return None
            else:
                self.tdb.tournament.insert(ser_tournament)
                return 1

    def sort_by_score(self):
        """
        :return:sorts players in tournament instance by score
        """
        scoreboard = []
        for player in self.players:
            pscore = [player, 0]
            for turns in self.tournees:
                for match in turns.matches:
                    if player in match[0]:
                        pscore[1] += match[0][1]
                    if player in match[1]:
                        pscore[1] += match[1][1]
            scoreboard.append(pscore)

        sortedscoreboard = sorted(scoreboard,
                                  key=lambda score: (score[1], score[0].elo),
                                  reverse=True)

        return sortedscoreboard

    def does_match_exist(self, new_match):
        for turns in self.tournees:
            for old_match in turns.matches:
                p_old = (old_match[0][0], old_match[1][0])
                p1_new = new_match[0][0]
                p2_new = new_match[1][0]
                if p1_new in p_old and p2_new in p_old:
                    return True
        else:
            return False

    def sort_by_elo(self):
        """
        :return: sorts players in tournament instance by score
        """
        sortedlist = sorted(self.players, key=lambda elosort: elosort.elo)
        return sortedlist
