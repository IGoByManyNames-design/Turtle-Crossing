# 🐢 Turtle Crossing Game

[![Play Online on Replit](https://img.shields.io/badge/Play%20Online-Replit-red?style=for-the-badge&logo=replit)](https://replit.com/@abhikgupta96/Turtle-Crossing)

A classic arcade-style road crossing game built using Python's `turtle` graphics library as part of the 100 Days of Code: Python Bootcamp (Day 23).


---

## 🎮 Overview

In **Turtle Crossing**, you control a turtle trying to safely cross a busy highway filled with randomly generated cars of varying lengths, colors, and speeds. Each successful crossing advances you to the next level, increasing the difficulty with faster traffic and more vehicles!

---

## ✨ Features

- **Dynamic Traffic System:** Cars spawn with randomized colors, lengths, and initial positions across multiple lanes.
- **Level Progression:** Each completed level increases car speed and traffic density.
- **Collision Detection:** Accurate bounding box logic detects crashes between the player turtle and oncoming cars.
- **Scoreboard & Game Over:** Displays the current level at the top of the screen and alerts the player upon collision.

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/turtle-crossing.git
   cd "turtle-crossing"
   ```
2. Launch the game:
   ```bash
   python main.py
   ```

---

## 🕹️ Controls

- **`Spacebar`**: Move the turtle forward.

---

## 📁 Project Structure

- `main.py`: Game loop, screen setup, collision checks, level tracking, and screen updates.
- `player.py`: Player class handling turtle movement, position reset, and game over screen.
- `car.py`: Car class and vehicle generator managing speed scaling, random sizing, and lane placement.
