class Views:
    """"""
    @staticmethod
    def tournament_already_true():
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
        fstring = f"\n\nHere's the list of all players:\n"
        print(fstring)

    @staticmethod
    def return_to_report_menu():
        """
        :return: waits for input to return to main menu
        """
        input("Press any key to return to report menu...")

    @staticmethod
    def list_all_tournaments(tournaments):
        """
        :param tournaments: all tournaments
        :return: all tournaments, formatted
        """
        print("\nHere's the list of all tournaments :")
        for tournament in tournaments:
            name = tournament[0]
            place = tournament[1]
            date = tournament[2]
            timetype = tournament[3]
            fstring = f"{place} {date} - {name} - {timetype}"
            print(fstring)
        input("\nPress any key to return to report menu..\n")

    @staticmethod
    def list_all_rounds(roundlist):
        """
        :param roundlist: List of all rounds
        :return: a view of all rounds from a tournament
        """
        for rounds in roundlist:
            print(rounds)
        input("\nPress any key to return to report menu..\n")

    @staticmethod
    def list_all_matches(matchlist):
        """
        :param matchlist: list of all matches
        :return: a view of all matches from a tournament
        """
        matchcount = 1
        roundcount = 1
        print('Round 1 : ')
        for match in matchlist:
            player1 = match[0]
            player2 = match[1]
            result1 = match[2]
            result2 = match[3]
            fstring = f"Match {matchcount} : {player1} [{result1}]" \
                      f" - [{result2}] {player2}"
            print(fstring)
            if matchcount % 4 == 0 and roundcount != 4:
                matchcount = 1
                roundcount += 1
                fstring2 = f"\nRound {roundcount} :"
                print(fstring2)
            else:
                matchcount += 1

        input("\nPress any key to return to report menu..\n")
