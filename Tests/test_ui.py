import sys
sys.path.append(".")
from GameMechanics import UI as uiClass
import unittest
import unittest.mock
from unittest.mock import patch, call

class TestMenuUi(unittest.TestCase):

    logo = """.------..------..------..------..------..------.     .------..------..------.
|C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |.-.  |W.--. ||A.--. ||R.--. |
| :/\: || (\/) || :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || :\/: || ()() |
| '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O| ((1)) '--'W|| '--'A|| '--'R|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'"""

    @patch('builtins.print')
    def testLogo(self, mock_print):
        uiClass.MenuUI.logo()
        mock_print.assert_called_with(TestMenuUi.logo)
        
    @patch('builtins.print')
    def testMainMenu(self, mock_print):
        uiClass.MenuUI.mainMenu()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Main menu":.^77}'),
                                                 call(f'\n{"1. New Game":^77}'),
                                                 call(f'{"2. Leaderboard":^80}'),
                                                 call(f'{"3. Rules":^74}'),
                                                 call(f'{"4. Exit":^73}')])

    @patch('builtins.print')
    def testPlayerNameSelector(self, mock_print):
        testName = "Test"
        inputName = uiClass.MenuUI.playerNameSelector()

        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Player name selector":.^77}')])
        self.assertEqual(testName, inputName)

    @patch('builtins.print')
    def testDifficultySelector(self, mock_print):
        uiClass.MenuUI.difficultySelector()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Difficulty selector":.^77}'),
                                                 call(f'\n{"1. Easy":^77}'),
                                                 call(f'{"2. Normal":^80}')])
        
    @patch('builtins.print')
    def testRules(self, mock_print):
        uiClass.MenuUI.rules()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Rules":.^77}'),
                                                 call("\nEach player starts with a balance of a 1000."),
                                                 call("One card each is dealt to the players."),
                                                 call("Card ranks (High -> Low): A K Q J 10 9 8 7 6 5 4 3 2"),
                                                 call("Whoever has the higher card win the wager they bet. One with a smaller card \nloses their bet."),
                                                 call("\nA tie occurs when the players each have cards of the same rank. In a tie the \nplayers have two options: \n1. A player can surrender, in which case the player loses half the bet.\n2. A player can go to war, in which case the player must double their stake."),
                                                 call("\nIf one of the players chose to go to war, but the other surrends, the \nplayer who chose to go to war gets 1.5x they bet back."),
                                                 call("In a war, the computer burns three cards before dealing each of them \nan additional card and the game continues as normal."),
                                                 call("\nA player wins if the other player runs out of their balance, \nor can leave at anytime by writing '0' in the bet window. ")])


class TestTableUi(unittest.TestCase):
    @patch('builtins.print')
    def testCardSymbolSpades(self, mock_print):
        uiClass.TableUI.cardSymbol(hand="Spades")
        self.assertEqual(mock_print.mock_calls, [call(f'{"*"} {"| :/⧹: |":^73} {"*"}'),
                                                 call(f'{"*"} {"| (⧹/) |":^73} {"*"}')])
    @patch('builtins.print')
    def testCardSymbolClubs(self, mock_print):
        uiClass.TableUI.cardSymbol(hand="Clubs")
        self.assertEqual(mock_print.mock_calls, [call(f'{"*"} {"| :(): |":^73} {"*"}'),
                                                 call(f'{"*"} {"| ()() |":^73} {"*"}')])
        
    @patch('builtins.print')
    def testCardSymbolDiamonds(self, mock_print):
        uiClass.TableUI.cardSymbol(hand="Diamonds")
        self.assertEqual(mock_print.mock_calls, [call(f'{"*"} {"| :/⧹: |":^73} {"*"}'),
                                                 call(f'{"*"} {"| :⧹/: |":^73} {"*"}')])

    @patch('builtins.print')
    def testCardSymbolHearts(self, mock_print):
        uiClass.TableUI.cardSymbol(hand="Hearts")
        self.assertEqual(mock_print.mock_calls, [call(f'{"*"} {"| (⧹/) |":^73} {"*"}'),
                                                 call(f'{"*"} {"| :⧹/: |":^73} {"*"}')])
    
    @patch('builtins.print')
    def testTable(self, mock_print):
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("6 of Clubs", 6)
        playerBalance = 550
        aiBalance = 450

        uiClass.TableUI.table(playerName, playerHand, aiHand, playerBalance, aiBalance)
        self.assertEqual(mock_print.mock_calls, [call(f'{"":*^77}'),
                                                 call(f'{"*"} {"AI’s balance: %d" % (aiBalance) :^73} {"*"}'),
                                                 call(f'{"*"} {"AI’s hand: %s" % (aiHand[0]) :^73} {"*"}'),
                                                 call(f'{"*"} {".------." :^73} {"*"}'),
                                                 call(f'{"*"} {"|%s.--. |" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}'),
                                                 call(f'{"*"} {"| :(): |":^73} {"*"}'),
                                                 call(f'{"*"} {"| ()() |":^73} {"*"}'),
                                                 call(f'{"*"} {"| `--’%s|" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}'),
                                                 call(f'{"*"} {"`------’":^73} {"*"}'),

                                                 call(f'{"*"} {"":^73} {"*"}'),
                                                 call(f'{"*"} {"":^73} {"*"}'),
                                                 call(f'{"*"} {"":^73} {"*"}'),
                                                 
                                                 call(f'{"*"} {".------.":^73} {"*"}'),
                                                 call(f'{"*"} {"|%s.--. |" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}'),
                                                 call(f'{"*"} {"| :/⧹: |":^73} {"*"}'),
                                                 call(f'{"*"} {"| :⧹/: |":^73} {"*"}'),
                                                 call(f'{"*"} {"| `--’%s|" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}'),
                                                 call(f'{"*"} {"`------’":^73} {"*"}'),
                                                 call(f'{"*"} {"%s’s hand: %s" % (playerName, playerHand[0]) :^73} {"*"}'),
                                                 call(f'{"*"} {"%s’s balance: %d" % (playerName, playerBalance) :^73} {"*"}'),
                                                 call(f'{"":*^77}')])
        
class TestBetUi(unittest.TestCase):
    def testBet(self):
        balance = 1000
        testBetAmount = 50

        inputBetAmount = uiClass.BetUI.bet(balance)
        self.assertEqual(testBetAmount, inputBetAmount)

    def testWar(self):
        testChoice = "WAR"

        inputChoice = uiClass.BetUI.war()
        self.assertEqual(testChoice, inputChoice)

    
# TODO Leaderboard test
        
class TestEndGameUi(unittest.TestCase):
    @patch('builtins.print')
    def testZeroBalance(self, mock_print):
        uiClass.EndGameUI.zeroBalance()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"You lost all your money. Better luck next time!":.^77}')])
        
    @patch('builtins.print')
    def testZeroBalance(self, mock_print):
        uiClass.EndGameUI.zeroBalance()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"You lost all your money. Better luck next time!":.^77}')])
        
    @patch('builtins.print')
    def testAiZeroBalance(self, mock_print):
        uiClass.EndGameUI.aiZeroBalance()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Congratulation! The AI lost all its money.":.^77}'),
                                                 call(f'{"+1000 points have been added to your score": ^77}')])
        
    @patch('builtins.print')
    def testNoCardsLeft(self, mock_print):
        uiClass.EndGameUI.noCardsLeft()
        self.assertEqual(mock_print.mock_calls, [call(TestMenuUi.logo),
                                                 call(f'{"Game ended! No more cards left in the deck":.^77}')])



class TestMidGameVisulas(unittest.TestCase):
    @patch('builtins.print')
    def testAiDecisionSurrend(self, mock_print):
        aiDecision = True
        uiClass.midGameVisuals.aiAction(aiDecision)
        self.assertEqual(mock_print.mock_calls, [call("Ai decided to surrend")])
    
    @patch('builtins.print')
    def testAiDecisionNotSurrend(self, mock_print):
        aiDecision = False
        uiClass.midGameVisuals.aiAction(aiDecision)
        self.assertEqual(mock_print.mock_calls, [call("Ai decided not to surrend")])

    @patch('builtins.print')
    def testWinIndicatorWin(self, mock_print):
        indicator = True
        uiClass.midGameVisuals.winIndecator(indicator)
        self.assertEqual(mock_print.mock_calls, [call("You won this round!")])

    @patch('builtins.print')
    def testWinIndicatorLose(self, mock_print):
        indicator = False
        uiClass.midGameVisuals.winIndecator(indicator)
        self.assertEqual(mock_print.mock_calls, [call("You lost this round!")])


class TestMenu(unittest.TestCase):
    def testCallMenu(self):
        testValues = ("Test", "Easy")
        returnedValues = uiClass.Menu.callMenu()

        self.assertEqual(testValues, returnedValues)
        




if __name__ == '__main__':
    unittest.main()

