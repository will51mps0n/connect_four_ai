# Connect Four AI

This project implements an AI agent that plays Connect Four using the Minimax algorithm with Alpha-Beta pruning. 

The AI is designed to make optimal moves and win against a human player or another AI, evaluating potential game states several moves ahead. 



## Features

- Minimax Algorithm with Alpha-Beta Pruning

- Heuristic evaluation of board states

- Configurable depth limit for difficulty adjustment

- Handles human vs AI gameplay



## Files

- **Agent.py**: Contains the Minimax AI agent logic

- **Connect4.py**: Game logic for Connect Four, board evaluation, and heuristics

- **Game.py**: Game interface logic

- **TTT.py**: (If applicable) Tic-Tac-Toe agent (can remove if not relevant)

- **test0.txt - test3.txt**: Test cases verifying AI behavior

- **requirements.txt**: Python dependencies (Pygame, Numpy)



## Setup

1. Clone the repo:

```bash
git clone https://github.com/will51mps0n/connect_four_ai.git
cd connect_four_ai
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```



## Running the Game

```bash
python Connect4.py
```

This launches the Connect Four game window. The AI will play against a human or another AI based on configuration.



## Tests

Test files are provided to verify AI's winning behavior. Run them individually if needed or check them as reference.



---

Created by Adam Simpson
> README.md

