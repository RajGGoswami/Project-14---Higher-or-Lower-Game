# Day 14 – Higher or Lower Game
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Working with lists of dictionaries
# - Comparing values stored in complex data structures
# - Using random selection while avoiding duplicates
# - Maintaining and updating game state (score)
# - Building a loop-driven comparison game
#
# This project recreates the "Higher or Lower" game,
# where the user guesses which option has more followers.

import os
import random
from art import logo, vs
from game_data import compare_data

# Initialize score and game state
score = 0
game_on = True

# Display game logo
print(logo)

# Randomly select the first comparison option
celeb_a = random.choice(compare_data)

while game_on:
    # Randomly select second option and ensure it's not the same as A
    celeb_b = random.choice(compare_data)
    while celeb_b == celeb_a:
        celeb_b = random.choice(compare_data)

    # Display comparison details (without follower count)
    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}")
    print(vs)
    print(f"Against B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")

    # Ask user to guess who has more followers
    follower_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Clear screen and reprint logo for clean UI
    os.system('cls')
    print(logo)

    # Compare follower counts based on user's guess
    if follower_guess == "A" and celeb_a['follower_count'] > celeb_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    elif follower_guess == "B" and celeb_a['follower_count'] < celeb_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False

    # Move B to A for the next round
    celeb_a = celeb_b
