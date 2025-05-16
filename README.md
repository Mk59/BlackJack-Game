# 🃏 Blackjack Game 🃏

Welcome to a **simple text-based Blackjack game** built in Python, where you play against the dealer!

## 🏁 How to Play:

The goal of Blackjack is to get as close as possible to **21 points** without going over. 

- **Number cards**: Worth their face value (2-10).
- **Face cards** (J, Q, K): Worth **10** points each.
- **Aces** (A): Worth **1** or **11** points (your choice).

---

## 🔄 Game Flow:

### 1. **Game Setup**:
   - You’ll be asked how many rounds you want to play.
   - In each round, both you and the dealer are dealt **two cards**.

### 2. **Your Turn**:
   - You can choose to **Hit** (draw a new card) or **Stand** (keep your current hand).
   - Keep drawing cards until you either **stand** or your hand value exceeds **21** (bust).

### 3. **Dealer’s Turn**:
   - After your turn, the dealer plays their hand.
   - The dealer **hits** until their hand value is **17** or greater.
   - If the dealer busts (goes over 21), **you win**!

### 4. **Winning the Round**:
   - The winner is determined by who has the hand closest to **21** without exceeding it:
     - **Player Busts**: Dealer wins.
     - **Dealer Busts**: Player wins.
     - **Blackjack**: If both the dealer and player get Blackjack, it's a **tie**.
     - **Final Comparison**: If no one busts, the hand with the higher value wins!

---

## 🖥️ Requirements:
- Python 3.x

---

## 🚀 How to Run:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blackjack-game.git
   cd blackjack-game

2. Run the game:

    ```bash
   python3 blackjack_game.py
   ```

---

## 🎮 Example Output:

```
How many games do you want to play? 3

******************************
Game 1 of 3
******************************
Your hand:
7 of diamonds
Q of clubs
Value: 17

Dealer's hand:
hidden
4 of clubs

Please choose 'Hit' or 'Stand': s

Dealer's hand:
A of hearts
4 of clubs
2 of spades

Final Results
Your hand: 17
Dealer's hand: 17

Tie! 

******************************
Game 2 of 3
******************************
Your hand:
9 of clubs
9 of hearts
Value: 18

Dealer's hand:
hidden
10 of diamonds

Please choose 'Hit' or 'Stand': s

Dealer's hand:
8 of hearts
10 of diamonds

Final Results
Your hand: 18
Dealer's hand: 18

Tie! 

******************************
Game 3 of 3
******************************
Your hand:
A of hearts
4 of diamonds
Value: 15

Dealer's hand:
hidden
8 of hearts

Please choose 'Hit' or 'Stand': h

Your hand:
A of hearts
4 of diamonds
7 of spades
Value: 12

Please choose 'Hit' or 'Stand': s

Dealer's hand:
3 of hearts
8 of hearts
J of spades

Dealer has blackjack. Dealer wins! 

Thanks for playing!

```

---

## 💡 Tips:

* Remember, **Aces** can be either 1 or 11, depending on your hand. Adjust your strategy accordingly!
* You can play as many rounds as you want. The game will continue until the rounds you specify are complete.

---
## 🎉 Thanks for Playing! 🎉
