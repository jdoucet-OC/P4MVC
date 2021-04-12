class InputViews:
    """"""
    @staticmethod
    def main_menu():
        """
        :return: menu view
        """
        print('\nWelcome!\n'
              'Chess Tournament Menu :\n'
              '[A] New Tournament\n'
              '[B] Resume Tournament\n'
              '[C] Players Management\n'
              '[D] Reports\n'
              '[X] Quit')

    @staticmethod
    def return_main_menu():
        """
        :return: use to return to main menu
        """
        print('[M] : Return to Main Menu')

    @staticmethod
    def tour_name():
        """
        :return: use when asking for tournament name
        """
        print("Tournament name :")

    @staticmethod
    def tour_place():
        """
        :return: use when asking for tournament place
        """
        print("Tournament place :")

    @staticmethod
    def tour_date():
        """
        :return: use when asking for tournament date
        """
        print("Tournament date : ")

    @staticmethod
    def day():
        """
        :return: use when asking for day
        """
        print("Day :")

    @staticmethod
    def month():
        """
        :return: use when asking for month
        """
        print("Month :")

    @staticmethod
    def year():
        """
        :return: use when asking for year
        """
        print("Year :")

    @staticmethod
    def timetype_list():
        """
        :return: use when asking for tournament timetype
        """
        print("Tournament TimeType :\n"
              "[1]Bullet - [2]Blitz - [3]Coup Rapide")

    @staticmethod
    def tour_description():
        """
        :return: use when asking for tournament description
        """
        print("Tournament description :")

    @staticmethod
    def expected_number():
        """
        :return: use with value error, expected a int
        """
        print("Expected a number")

    @staticmethod
    def add_player_menu():
        """
        :return: inserting players to tournament view
        """
        print("Add Players to tournament :")
        print("A: Add 8 Pre-selected Player ( demo )\n"
              "B: Pick 8 Players")

    @staticmethod
    def enter_match_results(player1, player2):
        """
        :param player1: player 1 from match
        :param player2: player 2 from match
        :return: a view to enter the results of a match
        """
        fstring = f"Winner : {player1} [A] or [B] {player2}" \
                  f"\nDraw : [C]"
        print(fstring)

    @staticmethod
    def player_manage_menu():
        """
        :return: player management menu
        """
        print('\n\nPlayer Management Menu:\n'
              '[A] Add new Player\n'
              '[B] Edit Player Elo\n'
              '[M] Return to Main Menu')

    @staticmethod
    def pick_player_edit():
        """
        :return: player picking menu
        """
        print("\n\nPick which player you want to edit :")

    @staticmethod
    def player_edit_list(ii, fname, lname, elo):
        """
        :param ii: player index, to choose from
        :param fname: player first name
        :param lname: player last name
        :param elo: player elo
        :return: player description
        """
        fstring = f"[{ii}] : {fname} {lname} - Elo = {elo}"
        print(fstring)

    @staticmethod
    def return_player_menu():
        """
        :return: return to main menu view
        """
        print('[M] : Return to Player Edit Menu\n')

    @staticmethod
    def edit_player_elo(fname, lname, elo):
        """
        :param fname: player first name
        :param lname: player last name
        :param elo: player elo
        :return: player elo edition menu
        """
        fstring = f"{fname} {lname} - Elo = {elo}" \
                  f"\nChoose new elo (min : 0, max : 3500) : "
        print(fstring)

    @staticmethod
    def player_add_menu():
        """
        :return: use for player addition menu
        """
        print('Player addition menu : \n')

    @staticmethod
    def player_first_name():
        """
        :return: use to ask for player first name
        """
        print('First Name :')

    @staticmethod
    def player_last_name():
        """
        :return: use to ask for player last name
        """
        print('Last name : ')

    @staticmethod
    def player_birthdate():
        """
        :return: use to ask for player birthdate
        """
        print("Birth Date : ")

    @staticmethod
    def player_genre():
        """
        :return: use to ask for player genre
        """
        print("Genre :")

    @staticmethod
    def player_elo():
        """
        :return: use to ask for player elo
        """
        print("Elo :")

    @staticmethod
    def continue_adding_choice():
        """
        :return: view to add another player or not
        """
        print('Would like to add another player?'
              '\n[Y]es/[N]o\n')

    @staticmethod
    def reports_menu_list():
        """
        :return: report menu choice view
        """
        print('List all players :\n'
              '  [A] : Alphabetical sort\n'
              '  [B] : Elo sort\n\n'
              'List all players in one tournament :\n'
              '  [C] : Alphabetical sort\n'
              '  [D] : Elo sort\n\n'
              '[E] List all tournaments\n'
              '[F] List all rounds in one tournament\n'
              '[G] List all matches in one tournament\n'
              '[M] Return to main menu')

    @staticmethod
    def tournament_choice():
        """
        :return: use when start the tournament picker
        """
        print("\n Pick one tournament :")

    @staticmethod
    def show_tournament_picker(tcount, place, date, name, timetype):
        """
        :param tcount: tournament index in tournament list
        :param place: tournament place
        :param date: tournament date
        :param name: tournament name
        :param timetype: tournament timetype
        :return: a view of a tournament
        """
        fstring = f"[{tcount}] : {place} {date}" \
                  f" - {name} - {timetype}"
        print(fstring)

    @staticmethod
    def show_player_picker(pcount, fname, lname, elo):
        """
        :param pcount: player index in player list
        :param fname: player first name
        :param lname: player last name
        :param elo: player elo
        :return: a view of a player
        """
        fstring = f"[{pcount}] : {fname} {lname} - Elo = {elo}"
        print(fstring)

    @staticmethod
    def show_player_chosen(chosen):
        """
        :param chosen: Chosen player
        :return: a view of a chosen player
        """
        print(chosen)

    @staticmethod
    def player_already_chosen():
        """
        :return:
        """
        print("\nPlayer already in picked in the list of players\n"
              "Choose Another One\n")
