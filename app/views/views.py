class Views:
    """"""
    def __init__(self):
        """"""
        pass

    @staticmethod
    def menu():
        """
        :return: input for choice menu
        """
        choicelist = ['a', 'b', 'c', 'd', 'x']
        choice = None
        while choice not in choicelist:
            print('\nWelcome!\n'
                  'Chess Tournament Menu :\n')
            choice = input('[A] New Tournament\n'
                           '[B] Resume Tournament\n'
                           '[C] Players Management\n'
                           '[D] Reports\n'
                           '[X] Quit\n').lower()
        return choice

    @staticmethod
    def new_tournament():
        """
        :return: inputs for tournament attributes
        """
        print("\n\nNew tournament, enter tournament attributes")
        tname = input("Tournament name : ")
        tplace = input("City : ")
        print("Date ( format : dd/mm/yyyy ) -")

        jdate = -2
        while jdate > 31 or jdate <= 0:
            try:
                jdate = int(input("Day : "))
            except ValueError:
                print('Expected a number\n')
        mdate = -2
        while mdate > 12 or mdate <= 0:
            try:
                mdate = int(input("Month : "))
            except ValueError:
                print('Expected a number\n')
        ydate = -2
        while ydate > 2500 or ydate <= 0:
            try:
                ydate = int(input("Year : "))
            except ValueError:
                print('Expected a number\n')
        if mdate < 10:
            mdate = f"0{mdate}"
        if jdate < 10:
            mdate = f"0{mdate}"
        tdate = "/".join([str(jdate), str(mdate), str(ydate)])

        to_list = ['Bullet', 'Blitz', 'Coup Rapide']
        choice_list = ['1', '2', '3']
        choice = None
        while choice not in choice_list:
            choice = input("TimeType :\n[1] Bullet\n[2] Blitz\n"
                           "[3] Coup Rapide\n")
        timetype = to_list[int(choice)-1]
        desc = input("Description : ")
        return tname, tplace, tdate, timetype, desc

    @staticmethod
    def tournament_already_true():
        print('Tournament already exists\n')

    @staticmethod
    def add_players():
        """
        :return: input of player type for tournament
        """
        print("\n\nAdd players")
        choicelist = ['a', 'b']
        players = None
        while players not in choicelist:
            players = input("A: Add 8 Pre-selected Player ( demo )\n"
                            "B: Pick 8 Players\n").lower()
        return players

    @staticmethod
    def show_pname(players):
        """
        :param players: player object
        :return: list of player names
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
        :param matches: list of matches, unformatted
        :return: list of matches to be played, formatted
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
        :param matches: matches just played
        :return: input of results to enter
        """
        results = []
        choice = None
        choicelist = ['a', 'b', 'c']
        for match in matches:
            while choice not in choicelist:
                player1 = match[0][0].lastName
                player2 = match[1][0].lastName
                fstring = f"Winner : {player1} [A] or [B] {player2}" \
                          f"\nDraw : [C]\n"
                choice = input(fstring).lower()
            results.append(choice)
            choice = None
        return results

    @staticmethod
    def show_results(matches):
        """
        :param matches: matches just played, with results
        :return: list of matches, with results
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
    def scoreboard(sortedscorelist):
        """
        :param sortedscorelist: list of matches, unformatted
        :return: list of matches to be played, formatted
        """
        print("Here's the scoreboard :\n")
        ranking = 1
        for match in sortedscorelist:
            playerln = match[0].lastName
            playerfn = match[0].firstName
            elo = match[0].elo
            score = match[1]
            fstring = f"{ranking} : [{score}] {playerfn} {playerln} - {elo}"
            print(fstring)
            ranking += 1
        input("\nPress any key to end tournament"
              " and return to main menu...\n")

    @staticmethod
    def go_next_round():
        """
        :return: input to go next round
        """
        input("Press any key to start next Round...\n")

    @staticmethod
    def tournament_end_view():
        """
        :return: input to return to main menu
        """
        print("\nThis is the end!")
        input("Press any Key to go to view scoreboard...")

    @staticmethod
    def resume_tournament():
        """
        :return: resume tournament loading
        """
        print("Resuming previous tournament...")

    @staticmethod
    def edit_players_menu():
        """
        :return: menu choice
        """

        choicelist = ['a', 'b', 'm']
        choice = None
        print('\n\nPlayer Management Menu:\n')

        while choice not in choicelist:
            choice = input('[A] Add new Player\n'
                           '[B] Edit Player Elo\n'
                           '[M] Return to Main Menu\n').lower()
        return choice

    @staticmethod
    def show_players_edit(players):
        """
        :param players: players object
        :return: list of players, to choose from
        """
        choicelist = ['m']
        choice = None
        for jj in range(0, len(players)+1):
            choicelist.append(str(jj))
        ii = 1
        print("\n\nPick which player you want to edit :\n")
        for player in players:
            lname = player.lastName
            fname = player.firstName
            elo = player.elo
            fstring = f"[{ii}] : {fname} {lname} - Elo = {elo}"
            print(fstring)
            ii += 1
        print('[M] : Return to Player Edit Menu\n')
        while choice not in choicelist:
            choice = input().lower()
        return choice

    @staticmethod
    def edit_elo(player):
        """
        :param player: player to edit elo from
        :return: input of new elo for player
        """
        lname = player.lastName
        fname = player.firstName
        elo = player.elo
        new_elo = -1
        while new_elo < 0 or new_elo > 3500:
            fstring = f"{fname} {lname} - Elo = {elo}" \
                      f"\nChoose new elo : "
            try:
                new_elo = int(input(fstring))
            except ValueError:
                print('Expected a number\n')
        return new_elo

    @staticmethod
    def add_player_view():
        """
        :return: list of attributes to save new Player
        """
        print('Player addition menu : \n')
        fname = input('First name : ')
        lname = input('Last name : ')

        print("Birth Date ( format : dd/mm/yyyy ) : ")
        jdate = -2
        while jdate > 31 or jdate <= 0:
            try:
                jdate = int(input("Day : "))
            except ValueError:
                print('Expected a number\n')
        mdate = -2
        while mdate > 12 or mdate <= 0:
            try:
                mdate = int(input("Month : "))
            except ValueError:
                print('Expected a number\n')
        ydate = -2
        while ydate > 2015 or ydate <= 1900:
            try:
                ydate = int(input("Year : "))
            except ValueError:
                print('Expected a number\n')
        if mdate < 10:
            mdate = f"0{mdate}"
        if jdate < 10:
            mdate = f"0{mdate}"
        bdate = "/".join([str(jdate), str(mdate), str(ydate)])
        genre = input('Genre : ')
        elo = 3200
        while elo > 3100 or elo <= 0:
            try:
                elo = int(input('Elo : '))
            except ValueError:
                print('Expected a number\n')
        return fname, lname, bdate, genre, elo

    @staticmethod
    def continue_adding():
        choice = None
        choicelist = ['y', 'n']
        while choice not in choicelist:
            choice = input('Would like to add another player?'
                           '\n[Y]es/[N]o\n').lower()
        return choice

    @staticmethod
    def reports_menu():
        """
        :return: input of menu to go to
        """
        choicelist = ['a', 'b', 'c', 'd',
                      'e', 'f', 'g', 'm']
        choice = None
        while choice not in choicelist:
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
                '[M] Return to main menu\n'
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
        mode_list = ["sorted alphebetically :",
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
        """
        :param tournaments: list of tournaments attributes
        :return: input of chosen tournament id
        """
        print("\n Pick one tournament :")
        ii = 0
        for tournament in tournaments:
            name = tournament[0]
            place = tournament[1]
            date = tournament[2]
            timetype = tournament[3]
            fstring = f"[{ii}] : {place} {date} - {name} - {timetype}"
            print(fstring)
            ii += 1
        strtourid = input()
        inttourid = int(strtourid)
        return inttourid

    @staticmethod
    def player_choice_picker(playerlist):
        """
        :param playerlist: list of players
        :return: input of chosen player ID's ( 8 )
        """
        inputs = []
        while len(inputs) < 8:
            for player in playerlist:
                try:
                    lname = player.lastName
                    fname = player.firstName
                    elo = player.elo
                    pid = player.get_player_id()
                    fstring = f"[{pid}] : {fname} {lname} - Elo = {elo}"
                    print(fstring)
                except AttributeError:
                    print(player)
            picker = input()
            inputs.append(int(picker))
            playerlist[int(picker)] = f"[{int(picker)}] : Already Chosen"
        return inputs

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
