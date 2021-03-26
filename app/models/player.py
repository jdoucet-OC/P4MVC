from ..models import managedb


class Player:
    """"""
    def __init__(self, fname, lname, bday, genre, elo):
        """
        :param fname: player first name
        :param lname: player last name
        :param bday: player birth date
        :param genre: player genre
        :param elo: player elo score
        """
        self.firstName = fname
        self.lastName = lname
        self.bDay = bday
        self.genre = genre
        self.elo = elo
        self.db = managedb.PlayerDb()
        self.insert_player()

    def insert_player(self):
        """
        :return: inserts players in DB, with ID
        """
        index = self.db.playersTable.__len__()
        ser_p1 = {
            'id': index,
            'lname': self.lastName.lower(),
            'fname': self.firstName.lower(),
            'bdate': self.bDay,
            'genre': self.genre,
            'elo': self.elo
        }
        cond1 = (self.db.query.lname == self.lastName.lower())
        cond2 = (self.db.query.fname == self.firstName.lower())
        cond3 = (self.db.query.bdate == self.bDay)

        search1 = self.db.playersTable.search(cond1 & cond2 & cond3)

        if not search1:
            self.db.playersTable.insert(ser_p1)

    def modify_elo(self, elo):
        """
        :param elo: new elo
        :return: updates DB with new player elo
        """
        cond1 = (self.db.query.lname == self.lastName.lower())
        cond2 = (self.db.query.fname == self.firstName.lower())
        cond3 = (self.db.query.bdate == self.bDay)
        self.db.playersTable.update({'elo': elo}, cond1 & cond2 & cond3)

    def get_player_id(self):
        """
        :return: player ID
        """
        cond1 = (self.db.query.lname == self.lastName.lower())
        cond2 = (self.db.query.fname == self.firstName.lower())
        cond3 = (self.db.query.bdate == self.bDay)

        search1 = self.db.playersTable.search(cond1 & cond2 & cond3)
        return search1[0]['id']

