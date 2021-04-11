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
    def tourname():
        """"""
        print("Tournament name :")

    @staticmethod
    def tourplace():
        """"""
        print("Tournament place :")

    @staticmethod
    def date():
        """"""
        print("Tournament date : ")

    @staticmethod
    def day():
        """"""
        print("Day :")

    @staticmethod
    def month():
        """"""
        print("Month :")

    @staticmethod
    def year():
        """"""
        print("Year :")

    @staticmethod
    def timetype_list():
        """"""
        print("Tournament TimeType :\n"
              "[1]Bullet - [2]Blitz - [3]Coup Rapide")

    @staticmethod
    def tourdescription():
        """"""
        print("Tournament description :")

    @staticmethod
    def expected_number():
        """"""
        print("Expected a number")

    @staticmethod
    def add_player_menu():
        """"""
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
        """"""
        print('\n\nPlayer Management Menu:\n'
              '[A] Add new Player\n'
              '[B] Edit Player Elo\n'
              '[M] Return to Main Menu')

    @staticmethod
    def pick_player_edit():
        print("\n\nPick which player you want to edit :")

    @staticmethod
    def player_edit_list(ii, fname, lname, elo):
        fstring = f"[{ii}] : {fname} {lname} - Elo = {elo}"
        print(fstring)

    @staticmethod
    def return_player_menu():
        print('[M] : Return to Player Edit Menu\n')

    @staticmethod
    def edit_player_elo(fname, lname, elo):
        fstring = f"{fname} {lname} - Elo = {elo}" \
                  f"\nChoose new elo (min : 0, max : 3500) : "
        print(fstring)
