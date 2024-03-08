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
                                                 call(f'{"3. Exit":^73}')])

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









if __name__ == '__main__':
    unittest.main()
