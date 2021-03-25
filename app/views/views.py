class Views:
    """"""
    def __init__(self):
        """"""
        pass

    @staticmethod
    def menu():
        """
        :return:
        """
        print('Chess Tournament Menu :\n')
        choice = input('A: New Tournament\n'
                       'B: Resume Tournament\n'
                       'C: Edit Players\n'
                       'D: Reports\n'
                       'Q: Quit\n').lower()
        return choice

    @staticmethod
    def new_tournament():
        """
        :return:
        """
        print("\n\nNew tournament, enter tournament attributes")
        tname = input("Tournament name : ")
        tplace = input("City : ")
        tdate = input("Date : ")
        timetype = input("TimeType : ")
        desc = input("Description : ")
        return tname, tplace, tdate, timetype, desc

    @staticmethod
    def add_players():
        """
        :return:
        """
        print("\n\nAdd players")
        players = input("A: Add 8 Pre-selected Player ( demo )\n"
                        "B: Pick 8 Players\n").lower()
        return players

    @staticmethod
    def show_pname(players):
        """
        :param players:
        :return:
        """
        ii = 1
        print("\n\nToday's players are :\n")
        for player in players:
            lname = player.lastName
            fname = player.firstName
            elo = player.elo
            fstring = f"Player {ii} : {fname} {lname} - Elo = {elo}"
            print(fstring)
            ii += 1
        input("\nPress any key to start first Round...\n")

    @staticmethod
    def show_elo_match(matches):
        """
        :param matches:
        :return:
        """
        for match in matches:
            player1 = match[0][0].lastName
            player2 = match[1][0].lastName
            elo1 = match[0][0].elo
            elo2 = match[1][0].elo
            score1 = match[0][1]
            score2 = match[1][1]
            fstring = f"{player1}({elo1}) [{score1}] vs" \
                      f" [{score2}] {player2}({elo2})"
            print(fstring)
        input("\nPress any key to enter results...\n")

    @staticmethod
    def enter_results(matches):
        """
        :param matches:
        :return:
        """
        results = []
        for match in matches:
            player1 = match[0][0].lastName
            player2 = match[1][0].lastName
            fstring = f"Winner : [A] {player1} or [B] {player2}" \
                      f"\nDraw : [C]\n"
            results.append(input(fstring).lower())
        return results

    @staticmethod
    def show_results(matches):
        """
        :param matches:
        :return:
        """
        ii = 1
        for match in matches:
            player1 = match[0][0].lastName
            player2 = match[1][0].lastName
            score1 = match[0][1]
            score2 = match[1][1]
            fstring = f"Match {ii}\n{player1} [{score1}]:" \
                      f"[{score2}] {player2}"
            print(fstring)
            ii += 1

    @staticmethod
    def go_next_round():
        """"""
        input("Press any key to start next Round...\n")

    @staticmethod
    def tournament_end_view():
        """"""
        print("This is the end!")
        input("Press any Key to go to main menu...")

    @staticmethod
    def resume_tournament():
        """
        :return:
        """
        print("Resuming previous tournament...")
        pass

    @staticmethod
    def show_players_edit(players):
        """
        :param players:
        :return:
        """
        ii = 1
        print("\n\nPick which player you want to edit :\n")
        for player in players:
            lname = player.lastName
            fname = player.firstName
            elo = player.elo
            fstring = f"[{ii}] : {fname} {lname} - Elo = {elo}"
            print(fstring)
            ii += 1
        print('[A] : Return to Menu\n')
        return input().lower()

    @staticmethod
    def edit_elo(player):
        """
        :param player:
        :return:
        """
        lname = player.lastName
        fname = player.firstName
        elo = player.elo
        fstring = f"{fname} {lname} - Elo = {elo}" \
                  f"\nChoose new elo : "
        elo = input(fstring)
        return elo

    @staticmethod
    def reports_menu():
        """
        :return:
        """
        choice = input(
            'List all players :\n'
            '  [A] : Alphabetical sort\n'
            '  [B] : Elo sort\n\n'
            'List all players in one tournament :\n'
            '  [C] : Alphabetical sort\n'
            '  [D] : Elo sort\n\n'
            '[E] List all tournaments\n'
            '[F] List all rounds in one tournament\n'
            '[G] List all matches in one tournament\n'
        ).lower()
        return choice

    @staticmethod
    def all_player_view(all_players, mode):
        """
        :param all_players: list of players
        :param mode: either alphabetical, or elo
        :return: view of all players
        """
        ii = 1
        mode_list = ["sorted alphebetically :"
                     "sorted by Elo :"]
        fstring = f"\n\nHere's the list of all players {mode_list[mode]} :\n"
        print(fstring)
        for player in all_players:
            lname = player.lastName
            fname = player.firstName
            elo = player.elo
            fstring = f"Player {ii} : {fname} {lname} - Elo = {elo}"
            print(fstring)
            ii += 1
        input("\nPress any key to return to report menu..\n")

    @staticmethod
    def tournament_choice_picker(tournaments):
        print("\n Chose one tournament :")
        ii = 0
        for tournament in tournaments:
            name = tournament[0]
            place = tournament[1]
            date = tournament[2]
            timetype = tournament[3]
            fstring = f"[{ii}] : {place} {date} - {name} - {timetype}"
            print(fstring)
        strtourid = input()
        inttourid = int(strtourid)
        return inttourid
