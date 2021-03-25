import os
from tinydb import TinyDB, Query
from .player import Player


class PlayerDb:
    """"""
    def __init__(self):
        """"""
        self.db = TinyDB(os.getcwd()+'\\app\\dbjson\\players.json')
        self.query = Query()
        self.playersTable = self.db.table('players')
        self.demoPlayerTable = self.db.table('demo')

    def return_demo(self):
        """
        :return: return list of demo players
        """
        playerlist = []
        for players in self.demoPlayerTable.all():
            lname = players['lname'].capitalize()
            fname = players['fname'].capitalize()
            bdate = players['bdate']
            genre = players['genre']
            elo = players['elo']
            playerlist.append(Player(fname, lname, bdate,
                                     genre, elo))
        return playerlist

    def return_players(self):
        """
        :return: return list of all players in player table
        """
        playerlist = []
        for players in self.playersTable.all():
            lname = players['lname'].capitalize()
            fname = players['fname'].capitalize()
            bdate = players['bdate']
            genre = players['genre']
            elo = players['elo']
            playerlist.append(Player(fname, lname, bdate,
                                     genre, elo))
        return playerlist

    def search_player_by_id(self, pid):
        cond1 = self.query.id == pid
        search1 = self.playersTable.search(cond1)
        return search1


class TournamentDb:
    """"""
    def __init__(self):
        """"""
        self.db = TinyDB(os.getcwd()+'\\app\\dbjson\\tournament.json')
        self.query = Query()
        self.tournament = self.db.table('tournament')
        self.rounds = self.db.table('rounds')
        self.matches = self.db.table('matches')

    def get_tournament_id(self, tournament):
        """
        :param tournament:
        :return:
        """
        cond1 = self.query.name == tournament.name.lower()
        cond2 = self.query.place == tournament.place.lower()
        cond3 = self.query.date == tournament.date

        search1 = self.tournament.search(cond1 & cond2 & cond3)
        return search1[0]['id']

    def return_player_tournament(self, tourid):
        """
        :param tourid:
        :return: créer un ID de joueur et faire la requette ASAP
        """
        search1 = self.query.tournament == tourid
        search2 = self.query.round == 0
        playerlist = []
        for item in self.matches.search(search1 & search2):
            playerlist.append(item['player1'])
            playerlist.append(item['player2'])
        return playerlist

    def return_tournaments(self):
        """
        :return:
        """
        tourlist = []
        for tournament in self.tournament.all():
            name = tournament['name'].capitalize()
            place = tournament['place'].capitalize()
            date = tournament['date']
            timetype = tournament['timeType']
            tourlist.append((name, place, date, timetype))
        return tourlist

    def return_rounds(self, tourid):
        """
        :param tourid:
        :return:
        """
        search1 = self.query.tournament == tourid
        roundlist = []
        for rounds in self.rounds.search(search1):
            round_id = rounds['id']
            tournament_id = rounds['tournament']
            name = rounds['name'].capitalize()
            roundlist.append((round_id, tournament_id, name))
        return roundlist

    def return_all_matches(self, tourid):
        """
        :param tourid:
        :return:
        """
        search1 = self.query.tournament == tourid
        matchlist = []
        for item in self.matches.search(search1):
            matchlist.append(item)
        return matchlist
