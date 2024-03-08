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
    scores = scoresClass.Scores()

    gameGoing = True
    # get previous scores from the cache
    scores.update()

    def regularGame():
        """Prints out Main menu"""
        Game.gameGoing = True
        menuResults = uiClass.Menu.callMenu()
        playerName = menuResults[0]
        difficulty = menuResults[1]

        """Creates player and AI object"""
        player = playerClass.Player(playerName)
        playerBalance = playerClass.Player.get_balance(player)
        Game.scores.add_player(player)

        ai = intellClass.Intelligence(Game.shuffledDeck, 1000)
        aiBalance = intellClass.Intelligence.getAiBalance(ai)

        
        while Game.gameGoing:
            betAmount = uiClass.BetUI.bet(playerBalance)

            """Exit midgame"""
            if betAmount == 0:
                Game.gameGoing = False
            else:
                """Checks if there are enough card left in deck"""
                enoughCards = Game.cardHand.enoughCardsInDeck(Game.shuffledDeck)
                if enoughCards:
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

                    # update the score of the player
                    Game.scores.update_player_balance(player, playerBalance)

                    """Prints out table"""
                    uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)
                    
                    """If the outcome is not a tie, writes out who won"""
                    if indicator != "Draw":
                        uiClass.midGameVisuals.winIndecator(indicator)
                    
                    """If the outcome is a tie, writes out ai's decision"""
                    if aiDecision != 3:
                        uiClass.midGameVisuals.aiAction(aiDecision)
                else:
                    """No card left in the deck"""
                    Game.gameGoing = False
                    uiClass.EndGameUI.noCardsLeft(playerBalance)
                    Game.startGameAgain() 

            """Game ending scenarios"""
            if playerBalance <= 0:
                """Player lost all of its balance""" 
                Game.gameGoing = False
                uiClass.EndGameUI.zeroBalance()
                Game.startGameAgain()

            elif aiBalance <= 0:
                """Ai lost all of its balance"""
                Game.gameGoing = False
                uiClass.EndGameUI.aiZeroBalance()

                # add 1000$ to the balance because he won
                Game.scores.update_player_balance(player, playerBalance + 1000)

                Game.startGameAgain()
        
        Game.gameGoing = False
        menuResults = uiClass.Menu.callMenu()
    
    """Check if AI has enough balance"""
    def aiHasEnoughBalance(betAmount, aiBalance):
        allInCheck = betClass.Bet.goAllIn(Game.bet, aiBalance, betAmount)
        aiBetAmount = allInCheck[0]

        return aiBetAmount



    """Decides who won the round"""
    def whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, shuffledDeck, difficulty, ai, aiDecision):
        indicator = True
        uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)

        aiBetAmount = Game.aiHasEnoughBalance(betAmount, aiBalance)

        """Round outcomes"""
        if playerHand[1] > aiHand[1]:
            """Player won"""
            playerBalance = Game.bet.cardHigher(playerBalance, betAmount)
            aiBalance = Game.bet.cardLower(aiBalance, aiBetAmount)

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision
        
        elif aiHand[1] > playerHand[1]:
            """Ai won"""
            indicator = False
            playerBalance = Game.bet.cardLower(playerBalance, betAmount)
            aiBalance = Game.bet.cardHigher(aiBalance, aiBetAmount)

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision
        
        elif playerHand[1] == aiHand[1]:
            """Checks if there are enough cards for a war"""
            enoughCardsForWar = Game.cardHand.enoughCardsInDeckWar(Game.shuffledDeck)
            if enoughCardsForWar:
                """Its a tie, 'tie' method gets called"""
                results = Game.tie(playerName, betAmount, playerBalance, aiBalance, shuffledDeck, difficulty, ai)

                return results
            else:
                print("Not enough cards left in deck to initiate war! Bets refunded")
                time.sleep(5)
                indicator = "Draw"
                return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision

    """Checks wether the player or the AI would like to go to war"""
    def tie(playerName, betAmount, playerBalance, aiBalance, shuffledDeck, difficulty, ai):
        choice = uiClass.BetUI.war()

        """Checks if player has enough balance to go to war"""
        if choice.upper() == "WAR":
            hasEnoughBalance = betClass.Bet.enoughBalance(Game.bet, betAmount*2, playerBalance)
            if not hasEnoughBalance:
                print("You don't have enough balance to go to war! You must surrend!")
                time.sleep(5)
                choice = "SURREND"

        """Checks if AI has enough balance to go to war"""       
        aiHasEnoughBalance = betClass.Bet.enoughBalance(Game.bet, betAmount*2, aiBalance)
        if not aiHasEnoughBalance:
            print("AI doesn't have enough balance to go to war! It must surrend!")
            time.sleep(5)
            aiChoice = True
        else:
            """AI decision based on the selected difficulty"""
            if difficulty == "Easy":
                aiChoice = intellClass.Intelligence.decideSurrenderEasyMode(ai)
            else:
                aiChoice = intellClass.Intelligence.decideSurrenderMediumMode(ai, shuffledDeck)

        aiBetAmount = Game.aiHasEnoughBalance(betAmount, aiBalance)

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
                aiBalance = Game.bet.surrend(aiBalance, aiBetAmount)
                indicator = "Draw"

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision


        elif choice.upper() == "SURREND":
            """Player chose to surrend"""
            if aiChoice == False:
                """AI chose to go to war"""
                aiDecision = 0
                aiBalance += aiBetAmount * 1.5
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                indicator = "Draw"

            else:
                """AI chose to surrend"""
                aiDecision = 1
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                aiBalance = Game.bet.surrend(aiBalance, aiBetAmount)
                indicator = "Draw"

            return playerBalance, shuffledDeck, aiBalance, indicator, aiDecision

    """Start the game again from the beginning"""
    def startGameAgain():
        # save scores to cache (object serialization)
        Game.scores.save()
        Game.gameGoing = False

        choice = input(print("Would you like to start again? (y/n): "))
        if choice == "y":
            Game.shuffledDeck = Game.deck.shuffleDeck()
            Game.regularGame()
            
    

    
