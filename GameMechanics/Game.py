import sys
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
    cards = cardClass.Card()
    deck = deckClass.Deck(cards)
    shuffledDeck = deck.shuffleDeck()
    cardHand = cardHandClass.CardHand(shuffledDeck)
    bet = betClass.Bet()

    def regularGame():
        menuResults = uiClass.Menu.callMenu()
        playerName = menuResults[0]
        difficulty = menuResults[1]

        score = scoresClass.Scores()
        player = playerClass.Player(playerName, score, 1000)
        playerBalance = playerClass.Player.getPlayerBalance(player)

        ai = intellClass.Intelligence(difficulty, Game.shuffledDeck)

        gameGoing = True
        while gameGoing:
            betAmount = uiClass.BetUI.bet(playerBalance)

            if betAmount == 0:
                gameGoing = False
            else:
                draws = Game.cardHand.drawCard(Game.shuffledDeck)
                playerHand = draws[0]
                aiHand = draws[1]
                shuffledDeck = draws[2]

                
                results = Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, betAmount, shuffledDeck)
                playerBalance = results[0]
                shuffledDeck = results[1]
                uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance)
            

            if not shuffledDeck or playerBalance <= 0:
                gameGoing = False
        
        menuResults = uiClass.Menu.callMenu()


    def whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, betAmount, shuffledDeck):
        uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance)
        if playerHand[1] > aiHand[1]:
            playerBalance = Game.bet.cardHigher(playerBalance, betAmount)
            return playerBalance, shuffledDeck
        elif aiHand[1] > playerHand[1]:
            playerBalance = Game.bet.cardLower(playerBalance, betAmount)
            return playerBalance, shuffledDeck
        elif playerHand[1] == aiHand[1]:
            results = Game.tie(playerName, betAmount, playerBalance, shuffledDeck)
            return results


    def tie(playerName, betAmount, playerBalance, shuffledDeck):
        choice = uiClass.BetUI.war()
        print("Teszt: %d" % playerBalance)
        if choice.upper() == "WAR":
            betAmount = Game.bet.war(betAmount)
            shuffledDeck = Game.deck.burnCard(shuffledDeck)
            draws = Game.cardHand.drawCard(shuffledDeck)
            playerHand = draws[0]
            aiHand = draws[1]
            shuffledDeck = draws[2]
            
            results = Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, betAmount, shuffledDeck)
            playerBalance = results[0]
            shuffledDeck = results[1]

            return playerBalance, shuffledDeck

        elif choice.upper() == "SURREND":
            playerBalance = Game.bet.surrend(playerBalance, betAmount)
            return playerBalance, shuffledDeck


    
Game.regularGame()
    

    
