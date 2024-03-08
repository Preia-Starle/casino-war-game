import os
import sys
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass
from GameMechanics import Bet as betClass
from GameMechanics import Scores as scoresClass

"""Prints out Menu uis"""
class MenuUI:
    """Prints out logo"""
    def logo():
        os.system('cls||clear')
        print(""".------..------..------..------..------..------.     .------..------..------.
|C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |.-.  |W.--. ||A.--. ||R.--. |
| :/\: || (\/) || :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || :\/: || ()() |
| '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O| ((1)) '--'W|| '--'A|| '--'R|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'""")
    
    """Prints out main menu"""
    def mainMenu():
        MenuUI.logo()
        print(f'{"Main menu":.^77}')
        print(f'\n{"1. New Game":^77}')
        print(f'{"2. Leaderboard":^80}')
        print(f'{"3. Rules":^74}')
        print(f'{"4. Exit":^73}')

    """Prints out player name selector"""
    def playerNameSelector():
        MenuUI.logo()
        print(f'{"Player name selector":.^77}')
        playerName = input(f'\n{"Enter your name: "}')
        return playerName
    
    """Prints out difficulty selector"""
    def difficultySelector():
        MenuUI.logo()
        print(f'{"Difficulty selector":.^77}')
        print(f'\n{"1. Easy":^77}')
        print(f'{"2. Normal":^80}')

    """Prints out the rules for the game"""
    def rules():
        MenuUI.logo()
        print(f'{"Rules":.^77}')
        print("\nEach player starts with a balance of a 1000.")
        print("One card each is dealt to the players.")
        print("Card ranks (High -> Low): A K Q J 10 9 8 7 6 5 4 3 2")
        print("Whoever has the higher card win the wager they bet. One with a smaller card \nloses their bet.")
        print("\nA tie occurs when the players each have cards of the same rank. In a tie the \nplayers have two options: \n1. A player can surrender, in which case the player loses half the bet.\n2. A player can go to war, in which case the player must double their stake.")
        print("\nIf one of the players chose to go to war, but the other surrends, the \nplayer who chose to go to war gets 1.5x they bet back.")
        print("In a war, the computer burns three cards before dealing each of them \nan additional card and the game continues as normal.")
        print("\nA player wins if the other player runs out of their balance, \nor can leave at anytime by writing '0' in the bet window. ")


"""Prints out Table uis"""
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

    """Prints out table"""
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

"""Prints out Bet uis"""
class BetUI:
    """Asks the player how much they want to bet"""
    def bet(balance):
        betSelf = betClass.Bet
        hasEnoughBalance = False

        """Checks if the input is a number"""
        while not hasEnoughBalance:
            try:
                """Checks if the user has enough balance for the bet"""
                betAmount = int(input(f'\n{"How much would you like to bet? (0 - Quit) (Current ammount: %d):  " % balance}'))
                hasEnoughBalance = betSelf.enoughBalance(betSelf, betAmount, balance)
                if not hasEnoughBalance:
                    print("You don't have enough balance to make that bet!")
            except ValueError:
                hasEnoughBalance = False

        return betAmount
    
    """Asks the player is they want to go to war or not"""
    def war():
        choice = ""

        """Checks if the input is equal to 'war' or to 'surrend'"""
        while choice not in ('WAR', 'SURREND'):
            choice = input("Would you like to go to war or surrend? (War/Surrend) ")
            choice = choice.upper()

        return choice
    
"""Prints out Leaderboard ui"""
class LeaderboardUI:
    def leaderboard():
        MenuUI.logo()
        print(f'{"Leaderboard":.^77}')

        scores = scoresClass.Scores()
        scores.update()

        print(scores)
        
        
"""Prints out EndGame uis"""
class EndGameUI:
    """Happens when player has zero or less balance"""
    def zeroBalance():
        MenuUI.logo()
        print(f'{"You lost all your money. Better luck next time!":.^77}')
    
    """Happens when the AI has zero or less balance"""
    def aiZeroBalance():
        MenuUI.logo()
        print(f'{"Congratulation! The AI lost all its money.":.^77}')
        print(f'{"+1000 points have been added to your score": ^77}')

        # score updated in Game class

    """Happens when there is no more card left in the deck"""
    def noCardsLeft(playerBalance):
        MenuUI.logo()
        print(f'{"Game ended! No more cards left in the deck":.^77}')
        print(f'{"Your final balance: %d " % (playerBalance) :.^77}')

"""Prints out MidGame uis"""
class midGameVisuals:
    """Prints out AI's decision"""
    def aiAction(aiDecision):
        notSurrend = "Ai decided not to surrend"
        surrend = "Ai decided to surrend"
        print(surrend if aiDecision else notSurrend)

    """Prints out whether the player won or lost"""
    def winIndecator(indicator):
        win = "You won this round!"
        lose = "You lost this round!"
        print(win if indicator else lose)

"""Handles Menu"""
class Menu:
    def callMenu():
        c = cardClass.Card()
        d = deckClass.Deck(c)

        difficulty = ""
        menu = MenuUI
        leaderboard = LeaderboardUI
        keepMenu = True

        """Checks if input is a number"""
        while keepMenu:
            menu.mainMenu()
            try:
                choiceMenu = int(input("\n>>>>>> "))
                keepMenu = False
            except ValueError:
                keepMenu = True
        
        match choiceMenu:
            case 1:
                """Game starts"""
                playerName = menu.playerNameSelector()
                keepDiffMenu = True
                while keepDiffMenu:
                    """Checks if the input is a number"""
                    menu.difficultySelector()
                    try:
                        difficultyChoice = int(input("\n>>>>>> "))
                        if difficultyChoice == 1:
                            difficulty = "Easy"
                        elif difficultyChoice == 2:
                            difficulty = "Normal"
                        keepDiffMenu = False

                        return playerName, difficulty
                    except ValueError:
                        keepDiffMenu = True
            case 2:
                """Leaderboard shown"""
                keepLeaderboard = True
                while keepLeaderboard:
                    leaderboard.leaderboard()
                    print("Press '0' to go back")

                    try:
                        keepLeaderboard = False
                        choiceLeaderboard = int(input("\n>>>>>> "))
                        if choiceLeaderboard == 0:
                            Menu.callMenu()
                        else:
                            keepLeaderboard = True
                    except ValueError:
                        keepLeaderboard = True
            case 3:
                keepRules = True
                while keepRules:
                    menu.rules()
                    print("\nPress '0' to go back")

                    try:
                        keepRules = False
                        choiceRules = int(input("\n>>>>>> "))
                        if choiceRules == 0:
                            Menu.callMenu()
                        else:
                            keepRules = True
                    except ValueError:
                        keepRules = True

            case 4:

                pass
        
