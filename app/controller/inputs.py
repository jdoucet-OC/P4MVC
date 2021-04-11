class Input:
    """"""
    def __init__(self, view):
        """
        :param view: input views
        """
        self.inputview = view

    def choice_main_menu(self):
        self.inputview.main_menu()
        choice = input()
        choicelist = ['a', 'b', 'c', 'd', 'x']
        while choice not in choicelist:
            choice = input()
        index = choicelist.index(choice)
        return index

    def tournament_attr_inputs(self):
        """
        :return:
        """
        self.inputview.tour_name()
        name = input()
        self.inputview.tour_place()
        place = input()

        # date builder, with exception catcher
        jdate = -2
        self.inputview.tour_date()
        while jdate > 31 or jdate <= 0:
            try:
                self.inputview.day()
                jdate = int(input())
            except ValueError:
                self.inputview.expected_number()
        mdate = -2
        while mdate > 12 or mdate <= 0:
            try:
                self.inputview.month()
                mdate = int(input())
            except ValueError:
                self.inputview.expected_number()
        ydate = -2
        while ydate > 2500 or ydate <= 0:
            try:
                self.inputview.year()
                ydate = int(input())
            except ValueError:
                self.inputview.expected_number()
        if mdate < 10:
            mdate = f"0{mdate}"
        if jdate < 10:
            mdate = f"0{mdate}"
        tdate = "/".join([str(jdate), str(mdate), str(ydate)])

        # time Type choice list
        self.inputview.timetype_list()
        to_list = ['Bullet', 'Blitz', 'Coup Rapide']
        choice_list = [1, 2, 3]
        timetype = None
        while timetype not in choice_list:
            timetype = int(input())
        timetype = to_list[timetype - 1]

        # description
        self.inputview.tour_description()
        description = input()
        return name, place, tdate, timetype, description

    def add_players(self):
        """
        :return: input of player type for tournament
        """
        self.inputview.add_player_menu()
        choicelist = ['a', 'b']
        players = None
        while players not in choicelist:
            players = input().lower()
        return players

    def enter_results(self, matches):
        """
        :param matches: matches just played
        :return: input of results to enter
        """
        results = []
        choice = None
        choicelist = ['a', 'b', 'c']
        for match in matches:
            player1 = match[0][0].lastName
            player2 = match[1][0].lastName
            self.inputview.enter_match_results(player1, player2)
            while choice not in choicelist:
                choice = input().lower()
            results.append(choice)
            choice = None
        return results

    def edit_players_menu(self):
        """
        :return: menu choice
        """
        self.inputview.player_manage_menu()
        choicelist = ['a', 'b', 'm']
        choice = None
        while choice not in choicelist:
            choice = input().lower()
        index = choicelist.index(choice)
        return index

    def show_players_edit(self, players):
        """
        :param players: players object
        :return: list of players, to choose from
        """
        choicelist = ['m']
        choice = None
        for jj in range(0, len(players)+1):
            choicelist.append(str(jj))
        ii = 1
        self.inputview.pick_player_edit()
        for player in players:
            lname = player.lastName
            fname = player.firstName
            elo = player.elo
            self.inputview.player_edit_list(ii, fname, lname, elo)
            ii += 1
        self.inputview.return_player_menu()
        while choice not in choicelist:
            choice = input().lower()
        return choice

    def edit_elo(self, player):
        """
        :param player: player to edit elo from
        :return: input of new elo for player
        """
        lname = player.lastName
        fname = player.firstName
        elo = player.elo
        new_elo = -1
        self.inputview.edit_player_elo(fname, lname, elo)
        while new_elo < 0 or new_elo > 3500:
            try:
                new_elo = int(input())
            except ValueError:
                self.inputview.expected_number()
        return new_elo

    def add_player_view(self):
        """
        :return: list of attributes to save new Player
        """
        self.inputview.player_first_name()
        fname = input()
        self.inputview.player_last_name()
        lname = input()

        # date builder, with exception catcher
        jdate = -2
        self.inputview.player_birthdate()
        while jdate > 31 or jdate <= 0:
            try:
                self.inputview.day()
                jdate = int(input())
            except ValueError:
                self.inputview.expected_number()
        mdate = -2
        while mdate > 12 or mdate <= 0:
            try:
                self.inputview.month()
                mdate = int(input())
            except ValueError:
                self.inputview.expected_number()
        ydate = -2
        while ydate > 2500 or ydate <= 0:
            try:
                self.inputview.year()
                ydate = int(input())
            except ValueError:
                self.inputview.expected_number()
        if mdate < 10:
            mdate = f"0{mdate}"
        if jdate < 10:
            mdate = f"0{mdate}"
        bdate = "/".join([str(jdate), str(mdate), str(ydate)])

        # Genre and elo
        self.inputview.player_genre()
        genre = input('')
        elo = 3200

        while elo > 3100 or elo <= 0:
            try:
                self.inputview.player_elo()
                elo = int(input())
            except ValueError:
                self.inputview.expected_number()
        return fname, lname, bdate, genre, elo

    def continue_adding(self):
        """
        :return: input yes / no to continue adding players
        or not
        """
        choice = None
        choicelist = ['y', 'n']
        self.inputview.continue_adding_choice()
        while choice not in choicelist:
            choice = input().lower()
        return choice

    def reports_menu(self):
        """
        :return: input of menu to go to
        """
        choicelist = ['a', 'b', 'c', 'd',
                      'e', 'f', 'g', 'm']
        choice = None
        self.inputview.reports_menu_list()
        while choice not in choicelist:
            choice = input().lower()
        index = choicelist.index(choice)
        return index

    def tournament_choice_picker(self, tournaments):
        """
        :param tournaments: list of tournaments
        :return: a list of tournaments choice picker
        """
        choicelist = ['m']
        choice = None
        for jj in range(0, len(tournaments)):
            choicelist.append(str(jj))
        tcount = 0
        self.inputview.tournament_choice()
        for tournament in tournaments:
            name = tournament[0]
            place = tournament[1]
            date = tournament[2]
            timetype = tournament[3]
            self.inputview.show_tournament_picker(tcount, place,
                                                  date, name, timetype)
            tcount += 1
        self.inputview.return_main_menu()
        while choice not in choicelist:
            choice = input().lower()
        if choice == "m":
            return choice
        else:
            return int(choice)

    def player_choice_picker(self, playerlist):
        """
        :param playerlist: list of players
        :return: input of chosen player ID's ( 8 )
        """
        inputs = []
        picker = -10
        pcount = 0
        while len(inputs) < 8:
            for player in playerlist:
                try:
                    picker = -10
                    lname = player.lastName
                    fname = player.firstName
                    elo = player.elo
                    pcount = player.get_player_id()
                    self.inputview.show_player_picker(pcount,
                                                      fname, lname, elo)
                except AttributeError:
                    self.inputview.show_player_chosen(player)
            while picker < 0 or picker > pcount:
                try:
                    picker = int(input())
                except ValueError:
                    self.inputview.expected_number()
                    picker = -10
            if picker in inputs:
                self.inputview.player_already_chosen()
            else:
                inputs.append(picker)
                playerlist[picker] = f"[{picker}] : Already Chosen"
        return inputs
