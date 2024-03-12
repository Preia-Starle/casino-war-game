
# Casino War

The game is played with a standard 52 card deck. The cards are ranked in the same way that cards in poker games are ranked, with aces being the highest cards.

One card each is dealt to an AI and to a player. If the player's card is higher, they win the wager they bet. However, if the AI's card is higher, the player loses their bet.

A tie occurs when the ai and the player each have cards of the same rank. In a tie situation, the player has two options:

The player can surrender, in which case the player loses half the bet.  
The player can go to war, in which case the player must double their stake.

If the player continues play in view of a tie, the computer burns (discards) three cards before dealing each of them an additional card. If the player's card is ranked higher than the AI's, then the player wins the amount of their original wager only. If the Ai's card is ranked higher than the player's, the player loses their (doubled) wager.





## Authors

- [Tibor Blascsok](https://github.com/Btibor02)
- [Kate Arvay](https://github.com/Preia-Starle)
- [Antoine Geiger](https://github.com/tableba)



## Screenshots

<img width="561" alt="Screenshot 2024-03-10 at 12 31 21" src="https://github.com/Preia-Starle/casino-war-game/assets/136988961/ecfa67b7-a6de-4dc9-89c8-2d3468fb9f93">

<img width="566" alt="Screenshot 2024-03-10 at 12 31 42" src="https://github.com/Preia-Starle/casino-war-game/assets/136988961/d6aaa24f-7fa6-4288-a828-d6f831a83edf">

## Demo

- [YouTube video](https://www.youtube.com/watch?v=VoK2HDMjmGI)


## Installation

Use git clone to clone the repository

```bash
git clone https://github.com/Preia-Starle/casino-war-game
```


It is best to make a virtual environement (venv) first before installing dependencies.

Making virtual environement (venv)
```bash
make venv
```
And follow the instructions.

Installing necessary dependencies
```bash
make install
```

Run the game
```bash
make start
```
    

## Running Tests

To run tests, run the following command

```bash
make coverage
```

## Linting

To run linting

```bash
make flake8
```

or 

```bash
make pylint
```

## Documentation

Documentation is available and can be run with

```bash
make docs
```


## Clearing Files
To clear generated files while playing the game or generating documentation, run 

```bash
make clean
```

Or to clean the generated documentation
```bash
make clean-docs
```

## Mac/Linux

If there is a problem with python, try running
```bash
export PYTHON=python3
```
and then
```bash
make start
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

