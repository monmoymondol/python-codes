# ⚽ Football Game

A simple 2D football (soccer) game built with **Python** and **Pygame**.  
Two players compete to score goals within a timed match. Includes **score tracking**, **goal detection**, and a **match timer**.

---

## 🎮 Features
- Two players (Red vs Blue).
- Move, kick the ball, and score goals.
- Goal posts on both sides of the field.
- Automatic **goal detection** when the ball enters the goal area.
- **Scoreboard** showing current score.
- **Match timer** (default: 90 seconds).
- Final score displayed at the end of the match.

---

## 📂 Project Structure
football_game/                                                                                                                                 
├── assets/              # (optional) images/sounds                                                                                            
├── src/                                                                                                                                      
│   ├── main.py           # entry point                                                                                                        
│   ├── game.py           # game loop, scoring, timer                                                                                           
│   ├── player.py         # player class                                                                                                        
│   ├── ball.py           # ball class                                                                                                        
│   └── utils.py          # helpers (optional)                                                                                                
├── requirements.txt                                                                                                                        
└── README.md                                                                                                                             



---

## ⚙️ Requirements
- Python 3.8+
- Pygame

Install dependencies:
```bash
pip install pygame
```

### 🚀 How to Run
Clone or download this repository.

Navigate into the project folder:

bash
cd football_game
Run the game:

bash

python src/main.py

### 🎮 Controls

Player 1 (Red):

Move Up: W

Move Down: S

Move Left: A

Move Right: D

Player 2 (Blue):

Move Up: ↑

Move Down: ↓

Move Left: ←

Move Right: →

### 🏆 Gameplay
Kick the ball into the opponent’s goal (white rectangles on each side).

Each goal increases the scorer’s team score.

The match lasts 90 seconds (configurable).

When time runs out, the game ends and the final score is displayed.

### 📸 Screenshots
will adding soon

### 📝 License
This project is open-source and free to use for learning and personal projects.



