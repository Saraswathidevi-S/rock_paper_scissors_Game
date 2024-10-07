import random
choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

def play_game():
    user_score = 0
    comp_score = 0
    rounds = int(input("How many rounds would you like to play? "))
    for i in range(rounds):
        print("\nRound", i+1)
        user_input = user_Value()
        comp_input = computer_input()
        print(f"You chose: {choices[user_input]}")
        print(f"Computer chose: {choices[comp_input]}")
        result = check(user_input, comp_input)
        print(result)

        # check score
        if "You Win" in result:
            user_score += 1
        elif "You Lose" in result:
            comp_score += 1
    
    # Print Winner
    print(f"\nFinal Score -> You: {user_score}, Computer: {comp_score}\n")
    if user_score > comp_score:
        print("Congratulations, you won the game!")
    elif comp_score > user_score:
        print("Sorry, You lose the game!")
    else:
        print("The game is a tie!")
        
        
# User input function
def user_Value():
    user_choice = input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): ")
    while user_choice not in ['0', '1', '2']:
        user_choice = input("Invalid choice! Please enter 0 (Rock), 1 (Paper), or 2 (Scissors): ")
    return int(user_choice)

# Computer input function
def computer_input():
    return random.randint(0, 2)

# Check who is winner
def check(user_input, comp_input):
    if user_input==0 and comp_input==2:
        return("You Win!")
    elif user_input==2 and comp_input==0:
        return("You Lose!")
    elif user_input==comp_input:
        return("It's a tie!")
    elif user_input<comp_input:
        return("You Lose!")
    elif user_input>comp_input:
        return("You Win!")

print("Welcome to Rock, Paper, Scissors!")
play_game()
