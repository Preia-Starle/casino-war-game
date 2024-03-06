import sys, time
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass
from CardMechanics import CardHand as cardHandClass

from GameMechanics import Bet as betClass
from GameMechanics import Scores as scoresClass
from GameMechanics import UI as uiClass

from Players import Intelligence as intellClass
from Players import Player as playerClass

class Game:
    """Creates a deck with shuffled cards"""
    cards = cardClass.Card()
    deck = deckClass.Deck(cards)
    shuffledDeck = deck.shuffleDeck()
    cardHand = cardHandClass.CardHand(shuffledDeck)
    bet = betClass.Bet()

    def regularGame():
        """Prints out Main menu"""
        menuResults = uiClass.Menu.callMenu()
        playerName = menuResults[0]
        difficulty = menuResults[1]

        """Creates player and AI object"""
        score = scoresClass.Scores()
        player = playerClass.Player(playerName)
        playerBalance = playerClass.Player.get_balance(player)

        ai = intellClass.Intelligence(Game.shuffledDeck, 1000)
        aiBalance = intellClass.Intelligence.getAiBalance(ai)

        gameGoing = True
        while gameGoing:
            betAmount = uiClass.BetUI.bet(playerBalance)

            """Exit midgame"""
            if betAmount == 0:
                gameGoing = False
            else:
                """Draws a card for both the player and ai"""
                draws = Game.cardHand.drawCard(Game.shuffledDeck)
                playerHand = draws[0]
                aiHand = draws[1]
                shuffledDeck = draws[2]

                """Calls 'whosCardIsHigher' method and returned values gets assigned to variables"""
                results = Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, shuffledDeck, difficulty, ai, aiDecision=3)
                playerBalance = results[0]
                shuffledDeck = results[1]
                aiBalance = results[2]
                indicator = results[3]
                aiDecision = results[4]

                """Prints out table"""
                uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)
                
                """If the outcome is not a tie, writes out who won"""
                if indicator != "Draw":
                    uiClass.midGameVisuals.winIndecator(indicator)
                
                """If the outcome is a tie, writes out ai's decision"""
                if aiDecision != 3:
                    uiClass.midGameVisuals.aiAction(aiDecision)
            

            """Game ending scenarios"""
            if not shuffledDeck:
                """No card left in the deck"""
                gameGoing = False
                uiClass.EndGameUI.noCardsLeft()
                Game.startGameAgain() 

            elif playerBalance <= 0:
                """Player lost all of its balance""" 
                gameGoing = False
                uiClass.EndGameUI.zeroBalance()
                Game.startGameAgain()

            elif aiBalance <= 0:
                """Ai lost all of its balance"""
                gameGoing = False
                uiClass.EndGameUI.aiZeroBalance()
                Game.startGameAgain()
        
        menuResults = uiClass.Menu.callMenu()


    """Decides who won the round"""
    def whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, shuffledDeck, difficulty, ai, aiDecision):
        indicator = True
        uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)



        """Round outcomes"""
        if playerHand[1] > aiHand[1]:
            """Player won"""
            playerBalance = Game.bet.cardHigher(playerBalance, betAmount)
            # ! Change it to aiBetAmount later
            aiBalance = Game.bet.cardLower(aiBalance, betAmount)

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision
        
        elif aiHand[1] > playerHand[1]:
            """Ai won"""
            indicator = False
            playerBalance = Game.bet.cardLower(playerBalance, betAmount)
            # ! Change it to aiBetAmount later
            aiBalance = Game.bet.cardHigher(aiBalance, betAmount)

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision
        
        elif playerHand[1] == aiHand[1]:
            """Its a tie, 'tie' method gets called"""
            results = Game.tie(playerName, betAmount, playerBalance, aiBalance, shuffledDeck, difficulty, ai)

            return results

    """Checks wether the player or the AI would like to go to war"""
    def tie(playerName, betAmount, playerBalance, aiBalance, shuffledDeck, difficulty, ai):
        # ! Exception handling
        choice = uiClass.BetUI.war()

        """Checks if player has enough balance to go to war"""
        if choice.upper() == "WAR":
            hasEnoughBalance = betClass.Bet.enoughBalance(Game.bet, betAmount*2, playerBalance)
            if not hasEnoughBalance:
                print("You don't have enough balance to go to war! You must surrend!")
                time.sleep(5)
                choice = "SURREND"


        """AI decision based on the selected difficulty"""
        if difficulty == "Easy":
            aiChoice = intellClass.Intelligence.decideSurrenderEasyMode(ai)
        else:
            aiChoice = intellClass.Intelligence.decideSurrenderMediumMode(ai, shuffledDeck)

        """Outcomes"""
        if choice.upper() == "WAR":
            """Player chose to go to war"""
            if aiChoice == False:
                """AI chose to go to war"""
                aiDecision = 0
                betAmount = Game.bet.war(betAmount)
                shuffledDeck = Game.deck.burnCard(shuffledDeck)
                draws = Game.cardHand.drawCard(shuffledDeck)

                playerHand = draws[0]
                aiHand = draws[1]
                shuffledDeck = draws[2]
                uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)
                
                results = Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, shuffledDeck, difficulty, ai, aiDecision)
                playerBalance = results[0]
                shuffledDeck = results[1]
                aiBalance = results[2]
                indicator = results[3]

            elif aiChoice == True:
                """AI chose to surrend"""
                aiDecision = 1
                playerBalance += betAmount * 1.5
                # ! Change it to aiBetAmount later
                aiBalance = Game.bet.surrend(aiBalance, betAmount)
                indicator = "Draw"

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision


        elif choice.upper() == "SURREND":
            """Player chose to surrend"""
            if aiChoice == False:
                """AI chose to go to war"""
                # ! Change it to aiBetAmount later
                aiDecision = 0
                aiBalance += betAmount * 1.5
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                indicator = "Draw"

            else:
                """AI chose to surrend"""
                aiDecision = 1
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                aiBalance = Game.bet.surrend(aiBalance, betAmount)
                indicator = "Draw"

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision

    """Start the game again from the beginning"""
    def startGameAgain():
        choice = input(print("Would you like to start again? (y/n): "))
        if choice == "y":
            Game.shuffledDeck = Game.deck.shuffleDeck()
            Game.regularGame()
    

    
