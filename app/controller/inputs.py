from ..views import views


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
        choice_list = ['a', 'b', 'c', 'd', 'x']
        while choice not in choice_list:
            choice = input()
        index = choice_list.index(choice)
        return index

    def tournament_attr_inputs(self):
        """
        :return:
        """
        self.inputview.tourname()
        name = input()
        self.inputview.tourplace()
        place = input()

        # date builder, with exception catcher
        jdate = -2
        self.inputview.date()
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
        self.inputview.tourdescription()
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
        return choice

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
