from art import logo, vs
from game_data import data
import random
import os

def clear_output():
    """clears system output"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def format_data(account):
    """takes the account data and returns printable format"""
    account_name = account["name"]x
    account_descriptioon = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descriptioon}, from {account_country}.")

def check_answer(guess, a_followers, b_followers):
    """take the user guess, follower count, and returns if they got it right"""
    if a_followers > b_followers: 
        return guess == "a"
    else:
        return guess == "b"

print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")
    
    guess = input("Who have more followers? Type 'A' or 'B': ").lower()
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear_output()
    print(logo)
    
    if is_correct:
        score += 1
        print("You're right!")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
