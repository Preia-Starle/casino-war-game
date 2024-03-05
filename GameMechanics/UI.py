import os
import sys
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass
from CardMechanics import CardHand as cardHandClass

class MenuUI:
    def logo():
        os.system('cls||clear')
        print(""".------..------..------..------..------..------.     .------..------..------.
|C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |.-.  |W.--. ||A.--. ||R.--. |
| :/\: || (\/) || :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || :\/: || ()() |
| '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O| ((1)) '--'W|| '--'A|| '--'R|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'""")
    
    def mainMenu():
        MenuUI.logo()
        print(f'{"Main menu":.^77}')
        print(f'\n{"1. New Game":^77}')
        print(f'{"2. Leaderboard":^80}')
        print(f'{"3. Exit":^73}')

    def playerNameSelector():
        MenuUI.logo()
        print(f'{"Player name selector":.^77}')
        playerName = input(f'\n{"Enter your name: "}')
        return playerName
    
    def difficultySelector():
        MenuUI.logo()
        print(f'{"Difficulty selector":.^77}')
        print(f'\n{"1. Easy":^77}')
        print(f'{"2. Normal":^80}')
        print(f'{"3. Hard":^77}')


class TableUI:
    """Prints out the right card symbol"""
    def cardSymbol(hand):
        match hand:
            case "Spades":
                print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
                print(f'{"*"} {"| (⧹/) |":^73} {"*"}')

            case "Clubs":
                print(f'{"*"} {"| :(): |":^73} {"*"}')
                print(f'{"*"} {"| ()() |":^73} {"*"}')
            
            case "Diamonds":
                print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
                print(f'{"*"} {"| :⧹/: |":^73} {"*"}')

            case "Hearts":
                print(f'{"*"} {"| (⧹/) |":^73} {"*"}')
                print(f'{"*"} {"| :⧹/: |":^73} {"*"}')

    def table(playerName, playerHand, aiHand, playerBalance, aiBalance):
        os.system('cls||clear')
        #Table Header
        print(f'{"":*^77}')

        """Prints out AI's card"""
        print(f'{"*"} {"AI’s balance: %d" % (aiBalance) :^73} {"*"}')
        print(f'{"*"} {"AI’s hand: %s" % (aiHand[0]) :^73} {"*"}')
        print(f'{"*"} {".------." :^73} {"*"}')
        print(f'{"*"} {"|%s.--. |" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}')
        TableUI.cardSymbol(aiHand[0].split(" ")[2])
        print(f'{"*"} {"| `--’%s|" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}')      
        print(f'{"*"} {"`------’":^73} {"*"}')

        for x in range(3):
            print(f'{"*"} {"":^73} {"*"}')

        """Prints out Player's card"""
        print(f'{"*"} {".------.":^73} {"*"}')
        print(f'{"*"} {"|%s.--. |" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}')
        TableUI.cardSymbol(playerHand[0].split(" ")[2])
        print(f'{"*"} {"| `--’%s|" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}')
        print(f'{"*"} {"`------’":^73} {"*"}')
        print(f'{"*"} {"%s’s hand: %s" % (playerName, playerHand[0]) :^73} {"*"}')
        print(f'{"*"} {"%s’s balance: %d" % (playerName, playerBalance) :^73} {"*"}')
        print(f'{"":*^77}')

class BetUI:
    def bet(balance):
        betAmount = int(input(f'\n{"How much would you like to bet? (0 - Quit) (Current ammount: %d):  " % balance}'))
        return betAmount
    
    def war():
        choice = input("Would you like to go to war or surrend? (War/Surrend) ")
        return choice
    

class LeaderboardUI:
    def leaderboard():
        MenuUI.logo()
        print(f'{"Main menu":.^77}')
        #for player in savedPlayer write out playerName and Score
        

class EndGameUI:
    def zeroBalance():
        MenuUI.logo()
        print(f'{"You lost all your money. Better luck next time!":.^77}')
    
    def aiZeroBalance():
        MenuUI.logo()
        print(f'{"Congratulation! The Computer lost all its money.":.^77}')
        print(f'{"+1000 points have been added to your score": ^77}')

    def noCardsLeft():
        MenuUI.logo()
        print(f'{"Game ended! No more cards left in the deck":.^77}')


class Menu:
    def callMenu():
        c = cardClass.Card()
        d = deckClass.Deck(c)

        difficulty = ""
        menu = MenuUI
        leaderboard = LeaderboardUI
        keepMenu = True

        while keepMenu:
            menu.mainMenu()
            choice = int(input("\n>>>>>> "))

            match choice:
                case 1:
                    playerName = menu.playerNameSelector()
                    keepDiffMenu = True
                    while keepDiffMenu:
                        menu.difficultySelector()
                        difficultyChoice = int(input("\n>>>>>> "))
                        if difficultyChoice == 1:
                            difficulty = "Easy"
                            keepDiffMenu = False
                        elif difficultyChoice == 2:
                            difficulty = "Normal"
                            keepDiffMenu = False
                        elif difficultyChoice == 3:
                            difficulty = "Hard"
                            keepDiffMenu = False
                    keepMenu = False
                    return playerName, difficulty
                
                case 2:
                    keepMenu = False
                    leaderboard.leaderboard()
                    print("Press 0 if you would like to go back")
                    choiceLeaderboard = int(input("\n>>>>>> "))
                    if choiceLeaderboard == 0:
                        Menu.callMenu()


                case 3:
                    # ! Saving the player score and name 
                    keepMenu = False