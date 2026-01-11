# Project-14---Higher-or-Lower-Game

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to build a Higher or Lower style comparison game where the user guesses which option has more followers.

**Project Overview** 

The Higher or Lower Game allows the user to:

Compare two public figures or platforms

Guess which one has more followers

Increase their score with correct guesses

End the game when a wrong guess is made

The game continues until the user guesses incorrectly.

**Project File Structure**

main.py
Contains the game logic, score tracking, and user interaction.

game_data.py
Stores the comparison data as a list of dictionaries.

art.py
Contains ASCII art for the game logo and VS symbol.

**Why this project exists**

This project helped me get comfortable working with nested data structures and comparing values inside dictionaries.

It also reinforced how to design a loop-based game that maintains state across rounds.

**What I learned**

How to work with lists of dictionaries

How to safely select random items without duplication

How to compare numeric values stored in dictionaries

How to maintain and update a score variable

How to structure repeated game logic

How to create a clean console experience

**How the code works (step-by-step)**

Display the game logo

Randomly select the first comparison option

Randomly select a second option and ensure it’s different

Display both options without follower counts

Ask the user to guess which has more followers

Compare follower counts based on the guess

Increase score if correct

End the game if incorrect

Carry the second option forward to the next round

**Example Output**

Compare A: Instagram, a Social media platform, from United States

Against B: Cristiano Ronaldo, a Footballer, from Portugal

Who has more followers? Type 'A' or 'B':
A

You're right! Current score: 1
