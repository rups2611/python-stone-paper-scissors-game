# python-stone-paper-scissors-game

This project is a Python-based implementation of the classic **Stone Paper Scissors** game, where you play against the computer. Below is a simple explanation of how the code works, step by step:

### **1. Game Setup**
- **Valid Choices**: The game recognizes three options: `"stone"`, `"paper"`, and `"scissors"`.
- **Random Choices**: The computer makes its choice randomly using Python's `random` module.

### **2. Welcome Message**
The game starts by displaying a welcome message and a set of instructions:
- The rules explain how each choice beats another:
  - Stone beats Scissors.
  - Scissors beats Paper.
  - Paper beats Stone.
- The game also informs the player that a tie occurs if both choose the same option.

### **3. User Input Validation**
  The player are prompted to choose one of the valid options:
- If you input something invalid (e.g., "rock" or "papers"), the program asks you to try again.
- This ensures the game only proceeds with valid inputs like `"stone"`, `"paper"`, or `"scissors"`.
- 
### **4. Computer's Turn**
The computer makes its choice randomly using the `random.choice()` function. This ensures the game is unpredictable and fair.

### **5. Comparing Choices**
The player’s choice and the computer’s choice are compared to determine the winner:
- **If it’s a tie**: The program displays, "It's a tie!!"
- **If the player wins**: The program explains why your choice beats the computer’s.
- **If the computer wins**: The program announces the computer as the winner.

### **6. Replay Option**
At the end of each round, the program asks:
  - **"Do you want to play again (y/n)?"**
  - If you type `"y"` (yes), the game restarts for another round.
  - If you type `"n"` (no), the game ends with a friendly goodbye message.

### **7. Exiting the Game**
When you decide to quit, the game displays a message thanking you for playing and ends gracefully.

### **Output of the game**

Welcome To Stone Paper Scissors Game!!
Instructions:
1. You will play against the computer.
2. You can choose one of the following options: 'stone', 'paper', or 'scissors'.
3. Stone beats Scissors.
4. Scissors beats Paper.
5. Paper beats Stone.
6. If you and the computer choose the same option, it's a tie.
Let's begin the game!

Enter the choice(stone,paper,scissors): stone
User chose: stone
Computer chose: scissors
User takes stone and computer takes scissors. Stone beats scissors and user wins.
Do you want to play again(y/n)? y

Enter the choice(stone,paper,scissors): paper
User chose: paper
Computer chose: stone
User takes paper and computer takes stone. Paper beats stone and user wins.
Do you want to play again(y/n)? n
You have ended the game.
See you next time!
