import os

class MenuUI:
    def logo():
        os.system('cls||clear')
        print(""".------..------..------..------..------..------.     .------..------..------.
|C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |.-.  |W.--. ||A.--. ||R.--. |
| :/\: || (\/) || :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || :\/: || ()() |
| '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O| ((1)) '--'W|| '--'A|| '--'R|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'""")
    
    def mainMenu(self):
        self.logo()
        print(f'{"Main menu":.^77}')
        print(f'\n{"1. New Game":^77}')
        print(f'{"2. Leaderboard":^80}')
        print(f'{"3. Exit":^73}')

    def playerNameSelector(self):
        self.logo()
        print(f'{"Player name selector":.^77}')
        playerName = input(f'\n{"Enter your name: "}')
        return playerName
    
    def difficultySelector(self):
        self.logo()
        print(f'{"Difficulty selector":.^77}')
        print(f'\n{"1. Easy":^77}')
        print(f'{"2. Normal":^80}')
        print(f'{"3. Hard":^77}')


class TableUI:
    def table():
        os.system('cls||clear')
        print(f'{"":*^77}')
        print(f'{"*":<15} {"AI hand"} {".------.":^29} {"*":>23}')
        print(f'{"*"} {"|C.--. |":^73} {"*"}')
        print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
        print(f'{"*"} {"| :⧹/: |":^73} {"*"}')
        print(f'{"*"} {"| `--’C|":^73} {"*"}')
        print(f'{"*"} {"`------’":^73} {"*"}')

        for x in range(3):
            print(f'{"*"} {"":^73} {"*"}')

        print(f'{"*"} {".------.":^73} {"*"}')
        print(f'{"*"} {"|C.--. |":^73} {"*"}')
        print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
        print(f'{"*"} {"| :⧹/: |":^73} {"*"}')
        print(f'{"*"} {"| `--’C|":^73} {"*"}')
        print(f'{"*":<22} {"`------’":^30} {"Player hand"} {"*":>11}')
        print(f'{"":*^77}')
        

u = MenuUI
u.mainMenu(u)