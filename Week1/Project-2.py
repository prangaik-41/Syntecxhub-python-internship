import random

def guess_game():
    print("\n Welcome to the Number Guessing Game!")

    best_score = None 

    while True:

        print("\nChoose Difficulty Level:")
        print("1. Easy   (1 - 20)")
        print("2. Medium (1 - 50)")
        print("3. Hard   (1 - 100)")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            max_num = 20
        elif choice == "2":
            max_num = 50
        elif choice == "3":
            max_num = 100
        else:
            print("Invalid choice, defaulting to Easy mode.")
            max_num = 20
        secret = random.randint(1, max_num)
        attempts = 0

        print(f"\nI have chosen a number between 1 and {max_num}. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess < secret:
                print("Higher!")
            elif guess > secret:
                print(" Lower!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New Best Score!")
        print(f"Best Score so far: {best_score} attempts.")

        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing! Goodbye!")
            break

guess_game()
