class Views:
    """"""
    @staticmethod
    def tournament_already_true():
        """
        :return: use when tournament already exists
        """
        print('Tournament already exists\n')

    @staticmethod
    def show_pname(pcount, lname, fname, elo):
        """
        :param pcount: player number n in the list of players
        :param lname: last name
        :param fname: first name
        :param elo: chess elo
        :return: player description view
        """
        fstring = f"Player {pcount} : {fname} {lname} - Elo = {elo}"
        print(fstring)

    @staticmethod
    def start_first_round():
        """
        :return: wait user input to start round
        """
        input("\nPress any key to start first Round...\n")

    @staticmethod
    def show_elo_match(p1, p2, s1, s2, elo1, elo2):
        """
        :param p1: player 1 last name
        :param p2: player 2 last name
        :param s1: score player 1
        :param s2: score player 2
        :param elo1: elo player 1
        :param elo2: elo player 2
        :return: view of upcoming match
        """
        fstring = f"{p1}({elo1}) [{s1}] vs" \
                  f" [{s2}] {p2}({elo2})"
        print(fstring)

    @staticmethod
    def start_results():
        """
        :return: waiting for input to enter results
        """
        input("\nPress any key to enter results\n")

    @staticmethod
    def show_results(mcount, p1, p2, s1, s2):
        """
        :param mcount: match index in the controller list
        :param p1: player 1
        :param p2: player 2
        :param s1: score 1
        :param s2: score2
        :return: match results
        """
        fstring = f"Match {mcount}\n{p1} [{s1}]:" \
                  f"[{s2}] {p2}"
        print(fstring)

    @staticmethod
    def start_scoreboard():
        """
        :return: scoreboard first view
        """
        print("\nHere's the scoreboard")

    @staticmethod
    def scoreboard(ranking, ln, fn, elo, score):
        """
        :param ranking: tournament rank
        :param ln: player first lame
        :param fn: player first name
        :param elo: player eloelo
        :param score: score in the tournament
        :return: tournament total scoreboard
        """
        fstring = f"{ranking} : [{score}] {ln} {fn} - {elo}"
        print(fstring)

    @staticmethod
    def end_scoreboard():
        """
        :return: scoreboard last view
        """
        input("\nPress any key to end tournament"
              " and return to main menu...\n")

    @staticmethod
    def go_next_round():
        """
        :return: waiting user input to go next round
        """
        input("Press any key to start next Round...\n")

    @staticmethod
    def tournament_end_view():
        """
        :return: waiting user input to see scoreboard
        """
        print("\nThis is the end!")
        input("Press any Key to go to view scoreboard...")

    @staticmethod
    def resume_tournament():
        """
        :return: view to resume a tournament
        """
        print("Resuming previous tournament...")

    @staticmethod
    def start_all_player_view():
        """
        :return: start view all players
        """
        print("\n\nHere's the list of all players:\n")

    @staticmethod
    def return_to_report_menu():
        """
        :return: waits for input to return to main menu
        """
        input("Press any key to return to report menu...")

    @staticmethod
    def start_all_tournament():
        """
        :return: use to start the list all tournaments
        """
        print("\nHere's the list of all tournaments :")

    @staticmethod
    def start_all_rounds():
        """
        :return: use to start the list all rounds
        """
        print("\nHere's the list of all the rounds :")

    @staticmethod
    def list_all_tournaments(place, date, name, timetype):
        """
        :param place: tournament place
        :param date: tournament date
        :param name: tournament name
        :param timetype: tournament timetype
        :return: tournament description list
        """

        fstring = f"{place} {date} - {name} - {timetype}"
        print(fstring)

    @staticmethod
    def list_all_rounds(rounds):
        """
        :param rounds: a round name
        :return: a round name
        """
        print(rounds)

    @staticmethod
    def list_all_matches(matchcount, player1, result1,
                         player2, result2,):
        """
        :param matchcount: match index in match list
        :param player1: player 1 firstname
        :param result1: result from match player 1
        :param player2: player 2 first name
        :param result2: result from match player 2
        :return: a view of a match
        """
        fstring = f"Match {matchcount} : {player1} [{result1}]" \
                  f" - [{result2}] {player2}"
        print(fstring)

    @staticmethod
    def all_matches_seperator(roundcount):
        """
        :param roundcount: round index in match list %4
        :return: a round name
        """
        fstring2 = f"\nRound {roundcount} :"
        print(fstring2)
