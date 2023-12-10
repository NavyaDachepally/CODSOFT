import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result, user_score, computer_score):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}")
    print(f"Scores - You: {user_score}  Computer: {computer_score}\n")

def rock_paper_scissors_game():
    print("Welcome to the Rock, Paper, Scissors Game!")

    user_score = 0
    computer_score = 0

    while True:
        print("\nOptions:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '4':
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ['1', '2', '3']:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            display_result(user_choice, computer_choice, result, user_score, computer_score)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
