import managedb


class Player:
    """"""

    def __init__(self, fname, lname, bday, genre, elo):
        """"""
        self.firstName = fname
        self.lastName = lname
        self.bDay = bday
        self.genre = genre
        self.elo = elo
        self.db = managedb.PlayerDb()
        self.insert_player()

    def insert_player(self):
        """
        :return:
        """
        ser_p1 = {
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
        """"""
        cond1 = (self.db.query.lname == self.lastName.lower())
        cond2 = (self.db.query.fname == self.firstName.lower())
        cond3 = (self.db.query.bdate == self.bDay)
        self.db.playersTable.update({'elo': elo}, cond1 & cond2 & cond3)

