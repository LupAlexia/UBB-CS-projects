# 🚀 Space Battle Game - Python application

A console-based terminal game where you control a space shuttle (`🚀`) and must destroy all hidden aliens (`👽`) while navigating around stars (`⭐`) using limited visibility and strategic movement.

This game was developed as part of the **Fundamental Programming** course from university.

## 🎮 Gameplay Overview

You play as a starship captain navigating an 8x8 galaxy. Your mission: eliminate all alien invaders using limited radar visibility.

- `🚀` — Your spaceship (USS Endeavour)
- `⭐` — Stars (impassable, visible by default)
- `👽` — Aliens (must be hit to win)
- Empty space — Move or fire here

You can **warp**, **fire**, or **cheat** (reveal the map).

### Win Condition
Destroy all alien ships by using strategic fire commands. Lose if you warp into an alien.

---

## 🧱 Features

- 8x8 dynamic board with hidden enemies and visible stars
- Intelligent warp system (can move diagonally, vertically, or horizontally)
- Shooting mechanics limited to visible adjacent tiles
- Cheat command to reveal the board (debugging or fun!)
- Automatic repositioning of aliens after a successful hit
- Text-based UI using `texttable` for a clear board layout

---

## 🕹️ Commands

You can type the following commands during gameplay:

| Command         | Example        | Description |
|----------------|----------------|-------------|
| `warp <cell>`  | `warp B3`      | Move ship to a new location (only if reachable) |
| `fire <cell>`  | `fire C4`      | Fire at target if within radar range |
| `cheat`        | `cheat`        | Reveal entire board (for debugging or cheating) |

---

## ⚠️ Rules

- You **can’t warp** into stars or unreachable cells.
- You **lose instantly** if you warp into an alien!
- You **can only fire** on visible (adjacent) cells.
- You **can’t shoot** stars — that's just rude.

---
##  How to Run
To run the project, simply execute the main.py file. 
