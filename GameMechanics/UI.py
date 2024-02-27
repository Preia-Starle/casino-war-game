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
    def table(playerName):
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
        print(f'{"*":<22} {"`------’":^30} {" %s’s hand" % (playerName)} {"*":>11}')
        print(f'{"":*^77}')
        

class Menu:
    def callMenu():
        difficulty = ""
        menu = MenuUI
        keepMenu = True

        while keepMenu:
            menu.mainMenu(menu)
            choice = int(input("\n>>>>>> "))

            match choice:
                case 1:
                    playerName = menu.playerNameSelector(menu)
                    menu.difficultySelector(menu)
                    difficultyChoice = int(input("\n>>>>>> "))
                    while difficultyChoice != 1 or 2 or 3:
                        if difficultyChoice == 1:
                            difficulty == "Easy"
                        elif difficultyChoice == 2:
                            difficulty == "Normal"
                        elif difficultyChoice == 3:
                            difficulty == "Hard"
                    keepMenu = False
                
                case 2:
                    pass

                case 3:
                    # ! Saving the player score and name 
                    keepMenu = False


m = Menu
m.callMenu()