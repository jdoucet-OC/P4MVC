from ..models import tournaments, round


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

    def run(self):
        """
        :return: main menu views
        """
        choice = self.view.menu()
        if choice == "a":
            self.new_tt()
        if choice == "b":
            self.resume_tt()
        if choice == "c":
            self.edit_players()
        if choice == "d":
            self.start_reports()
        if choice == "q":
            quit()

    def new_tt(self):
        """
        :return: creates a new tournament, from demo players, or
        sends user to player picker view
        """
        name, place, date, timetype, desc = self.view.new_tournament()
        tournament = tournaments.Tournament(name, place, date, timetype, desc)
        tournament.insert_tournament()
        players = self.view.add_players()
        if players == "a":
            self.demo_players(tournament)
        if players == "b":
            self.pick_players(tournament)

    def demo_players(self, tournament):
        """
        :param tournament: the currently played tournament instance
        :return: starts first round with demo players
        """
        tournament.players = self.pgetter.return_demo()
        tournament.players = tournament.sort_by_elo()
        self.view.show_pname(tournament.players)
        self.first_round(tournament)

    def first_round(self, tournament):
        """
        :param tournament: the currently played tournament instance
        :return: plays first round, and manages scores
        """
        middle = len(tournament.players) // 2
        lowerhalf = tournament.players[:middle]
        upperhalf = tournament.players[middle:]
        tour1 = []
        for ii in range(0, middle):
            tour1.append(([lowerhalf[ii], 0], [upperhalf[ii], 0]))
        round1 = round.Round('Round1', tour1)
        tournament.tournees.append(round1)

        # insertion du round 1
        round1.insert_round(tournament, 0)

        # Préparation du match
        self.view.show_elo_match(round1.matches)
        results = self.view.enter_results(round1.matches)
        self.process_results(tournament, results)

    def next_rounds(self, tournament):
        """
        :param tournament: the currently played tournament instance
        :return: plays the "next round" until round limit is
        reached
        """
        roundnumber = len(tournament.tournees)+1
        fstring = f"Round{roundnumber}"
        sortedscorelist = tournament.sort_by_score()
        nexttour = []
        for ii in range(0, len(sortedscorelist), 2):
            nexttour.append((sortedscorelist[ii], sortedscorelist[ii+1]))
        nextround = round.Round(fstring, nexttour)
        tournament.tournees.append(nextround)

        # insertion des rounds suivant
        indexr = roundnumber-1
        nextround.insert_round(tournament, indexr)

        # Préparation du match
        self.view.show_elo_match(nextround.matches)
        results = self.view.enter_results(nextround.matches)
        self.process_results(tournament, results)

    def process_results(self, tournament, results):
        """
        :param tournament: the currently played tournament instance
        :param results: results from the last played match
        :return: starts next round, or ends tournament if
        tournament round limit is reached
        """
        index = len(tournament.tournees)-1
        theround = tournament.tournees[index]
        theround.enter_scores(results)
        theround.insert_matches(tournament, index)
        if tournament.turns == len(tournament.tournees):
            self.view.show_results(theround.matches)
            # scoreboard à ajouter
            self.end_tournament()
        else:
            self.view.show_results(theround.matches)
            self.view.go_next_round()
            self.next_rounds(tournament)

    def end_tournament(self):
        """
        :return: ends tournament and returns to main menu
        """
        self.view.tournament_end_view()
        self.run()

    def pick_players(self, tournament):
        """
        :param tournament: the currently played tournament instance
        :return: user picks 8 players ID, and plays first round
        """
        choicelist = self.pgetter.return_players()
        pidlist = self.view.player_choice_picker(choicelist)
        playerlist = []
        for pid in pidlist:
            playerlist.append(self.pgetter.get_player_by_id(pid))
        tournament.players = playerlist
        tournament.players = tournament.sort_by_elo()
        self.view.show_pname(tournament.players)
        self.first_round(tournament)

    def edit_players(self):
        """
        :return: player elo edit, until "a" key press
        """
        players = self.pgetter.return_players()
        index = self.view.show_players_edit(players)
        if index == 'a':
            self.run()
        playerind = (players[int(index)-1])
        new_elo = self.view.edit_elo(playerind)
        playerind.modify_elo(int(new_elo))
        self.edit_players()

    def start_reports(self):
        """
        :return: reports menu choice picker
        """
        choice = self.view.reports_menu()
        choice_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        choice_func = [
            self.all_player_alpha_sort,
            self.all_players_elo_sort,
            self.tournament_alpha_sort,
            self.tournament_elo_sort,
            self.all_tournaments,
            self.list_all_rounds,
            self.list_all_matches
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
        tlist = self.tgetter.return_tournaments()
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
        tlist = self.tgetter.return_tournaments()
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
        tlist = self.tgetter.return_tournaments()
        self.view.list_all_tournaments(tlist)
        self.start_reports()

    def list_all_rounds(self):
        """
        :return: all rounds from one tournament
        """
        tlist = self.tgetter.return_tournaments()
        tourid = self.view.tournament_choice_picker(tlist)
        rlist = self.tgetter.return_rounds(tourid)
        for item in rlist:
            print(item)
        self.start_reports()

    def list_all_matches(self):
        """
        :return: all matches from one tournament
        """
        tlist = self.tgetter.return_tournaments()
        tourid = self.view.tournament_choice_picker(tlist)
        mlist = self.tgetter.return_all_matches(tourid)
        for item in mlist:
            print(item)
        self.start_reports()

    def resume_tt(self):
        """
        :return: resumes picked unfinished tournament
        """
        self.tgetter.return_unfinished_tournaments()
