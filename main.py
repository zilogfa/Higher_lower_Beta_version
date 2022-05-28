############# Developer: Ali Jafarbeglou


import random
from art import logo
from art import vs
from game_data import data


# question number maker
def question_num_maker():
    number = random.randint(0, len(data) - 1)
    return number


# question print maker base on question number
def question_maker(question):
    name = data[question]["name"]
    follower = data[question]["follower_count"]
    description = data[question]["description"]
    country = data[question]["country"]

    return f"{name}, {description}, from {country}"


def game():
    game_is_over = False
    correct_answer = False
    score = 0
    while game_is_over == False:
        print(f" yout Total score is {score}\n\n")
        print(logo)

        # question A
        if correct_answer == False:
            question_a = question_num_maker()
            print("Compare A: " + question_maker(question_a))
        else:
            print("Compare A: " + question_maker(question_a))

        print("\n" + vs + "\n")

        # Question B
        question_b = question_num_maker()
        print("Against B: " + question_maker(question_b))

        def compare():
            follower_a = data[question_a]["follower_count"]
            follower_b = data[question_b]["follower_count"]
            if follower_a > follower_b:
                return 'a'
            elif follower_b > follower_a:
                return 'b'

        user_answer = input("\n\n    - Who has more followers? Type 'A' or 'B': ").lower()

        if user_answer == compare():
            score += 1
            print(f"You're right! Current score: {score} ")
            if user_answer == "a":
                question_a = question_a
            else:
                question_a = question_b
            correct_answer = True
        else:
            print(f"Sorry, that's wrong. Final score: {score} ")
            game_is_over = True


game()







