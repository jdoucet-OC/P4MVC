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

    def get_player_by_id(self, pid):
        """
        :param pid: player ID
        :return: player objects, based on pid search
        """
        cond1 = self.query.id == pid
        search1 = self.playersTable.search(cond1)[0]
        lname = search1['lname'].capitalize()
        fname = search1['fname'].capitalize()
        bdate = search1['bdate']
        genre = search1['genre']
        elo = search1['elo']
        playerbyid = Player(fname, lname, bdate, genre, elo)
        return playerbyid


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
        :param tournament: tournament object
        :return: returns ID corresponding to tournament
        object search ( name, place, date )
        """
        cond1 = self.query.name == tournament.name.lower()
        cond2 = self.query.place == tournament.place.lower()
        cond3 = self.query.date == tournament.date

        search1 = self.tournament.search(cond1 & cond2 & cond3)
        return search1[0]['id']

    def return_player_tournament(self, tourid):
        """
        :param tourid: tournament ID
        :return: returns playerIDs corresponding to
        tour ID
        """
        search1 = self.query.tournament == tourid
        search2 = self.query.round == 0
        pidlist = []
        for item in self.matches.search(search1 & search2):
            pidlist.append(item['player1'])
            pidlist.append(item['player2'])
        return pidlist

    def return_all_tournaments_id(self):
        """
        :return: all tournaments
        """
        touridlist = []
        for tournament in self.tournament.all():
            touridlist.append(tournament['id'])
        return touridlist

    def return_unfinished_tourids(self):
        """
        :return: tournament ID of tournament with less than 16 matches
        """
        tourids = []
        unfinished_tourids = []
        for tournament in self.tournament.all():
            tourids.append(tournament['id'])
        for tourid in tourids:
            search1 = self.query.tournament == tourid
            matchlist = []
            for item in self.matches.search(search1):
                matchlist.append(item)
            if len(matchlist) < 16:
                unfinished_tourids.append(tourid)
        return unfinished_tourids

    def tourid_to_tour(self, touridlist):
        tourlist = []
        for tourid in touridlist:
            cond1 = self.query.id == tourid
            search1 = self.tournament.search(cond1)[0]
            name = search1['name'].capitalize()
            place = search1['place'].capitalize()
            date = search1['date']
            timetype = search1['timeType']
            desc = search1['description']
            tourlist.append((name, place, date, timetype, desc))
        return tourlist

    def return_rounds(self, tourid):
        """
        :param tourid: tournament ID
        :return: rounds corresponding to the tourid
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
        :param tourid: tournament ID
        :return: matches corresponding to the tourid
        """
        search1 = self.query.tournament == tourid
        matchlist = []
        for item in self.matches.search(search1):
            player1 = item['player1']
            player2 = item['player2']
            result1 = item['result1']
            result2 = item['result2']
            matchlist.append([player1, player2, result1, result2])
        return matchlist

    def where_were_we(self, tourid):
        search1 = self.query.tournament == tourid
        total_matches = int(len(self.matches.search(search1))/4)
        total_rounds = len(self.rounds.search(search1))
        if total_rounds != total_matches:
            roundid = total_rounds-1
            self.del_last_round(tourid, roundid)
        else:
            roundid = total_rounds
        print(roundid)

    def del_last_round(self, tourid, roundid):
        cond1 = self.query.tournament == tourid
        cond2 = self.query.id == roundid
        self.rounds.remove((cond1) & (cond2))
