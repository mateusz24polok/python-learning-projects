import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking about a number between 1 and 100.")

difficulty_input = None

while (difficulty_input != "easy" and difficulty_input != "hard" and difficulty_input != "quit"):
    difficulty_input = input(
"Choose a difficulty. Type 'easy' or 'hard' or 'quit' if you want to finish: ")


def get_attempts(difficulty_input):
    if difficulty_input == "easy":
        return 10
    elif difficulty_input == "hard":
        return 5
    else:
        return None


def guess_number_and_return_attempts(guessed_number, answer_number, attempts):
    if (guessed_number > answer_number):
        print("Your number is to high")
    elif (guessed_number < answer_number):
        print("You number is to low")
    else:
        print("You guessed the number !!!")
    return attempts - 1


def get_attempt_summary_message(guessed_number, answer_number, attempts):
    if guessed_number == answer_number:
        pass
    else:
        if attempts:
            print(
                f"You have {attempts} attempts remaining to guess the number")
        else:
            print("You have lost all your attempts to guess the number.")


answer_number = random.randint(0, 100)
guessed_number = None
attempts = get_attempts(difficulty_input)

while (not guessed_number or (guessed_number != answer_number and attempts)):
    guessed_number = int(input("Make a guess: "))
    attempts = guess_number_and_return_attempts(guessed_number, answer_number, attempts)
    get_attempt_summary_message(guessed_number, answer_number, attempts)
