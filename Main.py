from GameMechanics.UI import MenuUI, TableUI

def main():
    difficulty = ""
    menu = MenuUI
    table = TableUI
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



if __name__ == '__main__':
    main()

