from ..models import tournaments, round
from ..models import player


class Controller:
    """"""
    def __init__(self, view, pgetter, tgetter):
        """
        :param view: View object, allowing for controller
         to display views
        :param pgetter: player DB manager object from model
        :param tgetter: tournament DB manager object from model
        """
        self.view = view
        self.pgetter = pgetter
        self.tgetter = tgetter
        self.tournament = None

    def run(self):
        """
        :return: main menu views
        """
        choice = self.view.menu()
        choice_list = ['a', 'b', 'c', 'd', 'x']
        funcs_list = [self.new_tt, self.resume_tt,
                      self.edit_players,
                      self.start_reports, quit]
        for letter in choice_list:
            if choice == letter:
                index = choice_list.index(choice)
                funcs_list[index]()

    def new_tt(self):
        """
        :return: creates a new tournament, from demo players, or
        sends user to player picker view
        """
        insert = None
        while insert is None:
            name, place, date, timetype, desc = self.view.new_tournament()
            self.tournament = tournaments.Tournament(name, place,
                                                     date, timetype, desc)
            insert = self.tournament.insert_tournament()
            if insert is None:
                self.view.tournament_already_true()
        players = self.view.add_players()
        if players == "a":
            self.demo_players()
        if players == "b":
            self.pick_players()

    def demo_players(self):
        """
        :return: starts first round with demo players
        """
        self.tournament.players = self.pgetter.return_demo()
        self.tournament.players = self.tournament.sort_by_elo()
        self.view.show_pname(self.tournament.players)
        self.first_round()

    def first_round(self):
        """
        :return: plays first round, and manages scores
        """
        middle = len(self.tournament.players) // 2
        lowerhalf = self.tournament.players[:middle]
        upperhalf = self.tournament.players[middle:]
        tour1 = []
        # création du premier bracket
        for ii in range(0, middle):
            thematch = ([lowerhalf[ii], 0], [upperhalf[ii], 0])
            tour1.append(thematch)
        round1 = round.Round('Round1', tour1)
        self.tournament.tournees.append(round1)

        # insertion du round 1
        round1.insert_round(self.tournament, 0)

        # Préparation du match
        self.view.show_elo_match(round1.matches)
        results = self.view.enter_results(round1.matches)
        self.process_results(results)

    def next_rounds(self):
        """
        :return: plays the "next round" until round limit is
        reached
        """
        roundnumber = len(self.tournament.tournees)+1
        fstring = f"Round{roundnumber}"
        sortedscorelist = self.tournament.sort_by_score()
        nexttour = []
        # préparation des nexts brackets
        for ii in range(0, len(sortedscorelist), 2):
            thematch = (sortedscorelist[ii], sortedscorelist[ii + 1])
            # vérifier si le joueur 1 à déjà jouer avec le joueur 2
            if ii == 0:
                if self.tournament.does_match_exist(thematch):
                    sortedscorelist[1], sortedscorelist[2] =\
                        sortedscorelist[2], sortedscorelist[1]
                    thematch = (sortedscorelist[ii],
                                sortedscorelist[ii + 1])
            nexttour.append(thematch)
        nextround = round.Round(fstring, nexttour)
        self.tournament.tournees.append(nextround)

        # insertion des rounds suivant
        indexr = roundnumber-1
        nextround.insert_round(self.tournament, indexr)

        # Préparation du match
        self.view.show_elo_match(nextround.matches)
        results = self.view.enter_results(nextround.matches)
        self.process_results(results)

    def process_results(self, results):
        """
        :param results: results from the last played match
        :return: starts next round, or ends tournament if
        tournament round limit is reached
        """
        index = len(self.tournament.tournees)-1
        theround = self.tournament.tournees[index]
        theround.enter_scores(results)
        theround.insert_matches(self.tournament, index)
        if self.tournament.turns == \
                len(self.tournament.tournees):
            self.view.show_results(theround.matches)
            self.end_tournament()
        else:
            self.view.show_results(theround.matches)
            self.view.go_next_round()
            self.next_rounds()

    def end_tournament(self):
        """
        :return: ends tournament and returns to main menu
        """
        self.view.tournament_end_view()
        sortedscorelist = self.tournament.sort_by_score()
        self.view.scoreboard(sortedscorelist)
        self.run()

    def pick_players(self):
        """
        :return: user picks 8 players ID, and plays first round
        """
        choicelist = self.pgetter.return_players()
        pidlist = self.view.player_choice_picker(choicelist)
        playerlist = []
        for pid in pidlist:
            playerlist.append(self.pgetter.get_player_by_id(pid))
        self.tournament.players = playerlist
        self.tournament.players = self.tournament.sort_by_elo()
        self.view.show_pname(self.tournament.players)
        self.first_round()

    def edit_players(self):
        choice = self.view.edit_players_menu()
        choice_list = ['a', 'b', 'm']
        func_list = [self.add_players,
                     self.edit_elo_players,
                     self.run]

        for letter in choice_list:
            if choice == letter:
                index = choice_list.index(choice)
                func_list[index]()

    def add_players(self):
        fname, lname, bdate, genre, elo = self.view.add_player_view()
        newplayer = player.Player(fname, lname, bdate, genre, elo)
        newplayer.insert_player()
        choice = self.view.continue_adding()
        if choice == 'y':
            self.add_players()
        else:
            self.run()

    def edit_elo_players(self):
        """
        :return: player elo edit, until "a" key press
        """
        players = self.pgetter.return_players()
        index = self.view.show_players_edit(players)
        if index == 'm':
            self.edit_players()
        playerind = (players[int(index)-1])
        new_elo = self.view.edit_elo(playerind)
        playerind.modify_elo(new_elo)
        self.edit_elo_players()

    def start_reports(self):
        """
        :return: reports menu choice picker
        """
        choice = self.view.reports_menu()
        choice_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'm']
        choice_func = [
            self.all_player_alpha_sort,
            self.all_players_elo_sort,
            self.tournament_alpha_sort,
            self.tournament_elo_sort,
            self.all_tournaments,
            self.list_all_rounds,
            self.list_all_matches,
            self.run
        ]
        for letter in choice_list:
            if choice == letter:
                index = choice_list.index(choice)
                choice_func[index]()

    def all_player_alpha_sort(self):
        """
        :return:sends a list of all players to the view, sorted
        alphebetically
        """
        all_players = self.pgetter.return_players()
        all_players.sort(key=lambda x: x.lastName)
        self.view.all_player_view(all_players, 0)
        self.start_reports()

    def all_players_elo_sort(self):
        """
        :return: sends a list of all players to the view, sorted
        by elo
        """
        all_players = self.pgetter.return_players()
        all_players.sort(key=lambda x: x.elo, reverse=True)
        self.view.all_player_view(all_players, 1)
        self.start_reports()

    def tournament_alpha_sort(self):
        """
        :return: sends a list of all players in one tournament,
        sorted alphabetically
        """
        tidlist = self.tgetter.return_all_tournaments_id()
        tlist = self.tgetter.tourid_to_tour(tidlist)
        tourid = self.view.tournament_choice_picker(tlist)
        pidlist = self.tgetter.return_player_tournament(tourid)
        playerlist = []
        for pid in pidlist:
            playerlist.append(self.pgetter.get_player_by_id(pid))
        playerlist.sort(key=lambda x: x.lastName)
        self.view.all_player_view(playerlist, 0)
        self.start_reports()

    def tournament_elo_sort(self):
        """
        :return: sends a list of all players in one tournament,
        sorted by elo
        """
        tidlist = self.tgetter.return_all_tournaments_id()
        tlist = self.tgetter.tourid_to_tour(tidlist)
        tourid = self.view.tournament_choice_picker(tlist)
        pidlist = self.tgetter.return_player_tournament(tourid)
        playerlist = []
        for pid in pidlist:
            playerlist.append(self.pgetter.get_player_by_id(pid))
        playerlist.sort(key=lambda x: x.elo, reverse=True)
        self.view.all_player_view(playerlist, 1)
        self.start_reports()

    def all_tournaments(self):
        """
        :return: all tournaments
        """
        tidlist = self.tgetter.return_all_tournaments_id()
        tlist = self.tgetter.tourid_to_tour(tidlist)
        self.view.list_all_tournaments(tlist)
        self.start_reports()

    def list_all_rounds(self):
        """
        :return: all rounds from one tournament
        """
        tidlist = self.tgetter.return_all_tournaments_id()
        tlist = self.tgetter.tourid_to_tour(tidlist)
        tourid = self.view.tournament_choice_picker(tlist)
        rlist = self.tgetter.return_rounds(tourid)
        self.view.list_all_rounds(rlist)
        self.start_reports()

    def list_all_matches(self):
        """
        :return: all matches from one tournament
        """
        tidlist = self.tgetter.return_all_tournaments_id()
        tlist = self.tgetter.tourid_to_tour(tidlist)
        tourid = self.view.tournament_choice_picker(tlist)
        mlist = self.tgetter.return_all_matches(tourid)
        for match in mlist:
            pid1toid = self.pgetter.get_player_by_id(match[0])
            match[0] = pid1toid.firstName
            pid2toid = self.pgetter.get_player_by_id(match[1])
            match[1] = pid2toid.firstName
        self.view.list_all_matches(mlist)
        self.start_reports()

    def resume_tt(self):
        """
        :return: resumes the chosen unfinished tournament
        """
        unfin = self.tgetter.return_unfinished_tourids()
        tlist = self.tgetter.tourid_to_tour(unfin)
        choice = self.view.tournament_choice_picker(tlist)
        tourid = unfin[choice]
        name, place, date, timetype, desc = tlist[choice]
        self.tournament = tournaments.Tournament(name, place, date,
                                                 timetype, desc)
        roundid = self.tgetter.where_were_we(tourid)
        print(roundid)
