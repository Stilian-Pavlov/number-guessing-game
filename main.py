import random
wanted_number=random.randint(1,100)


def ask_user():
    user_choice=input("Do you want to play  (Yes/No)?").lower()
    return user_choice

def my_game():
    user_number = int(input("Please select a number between 1 and 100: "))
    while True:
        if user_number!=wanted_number:
            user_choice=input("Do you want to continue trying? (Yes/No)").lower()
            if user_choice=="yes":
                user_number = int(input("Please select a number between 1 and 100: "))

            else:
                print("You didn't guess the number!")
                print(f"The number was {wanted_number}")
                exit()

        if user_number==wanted_number:
            print("Congratulations you guessed the number!!!")
            break

while True:
    if ask_user()=="yes":
        my_game()
    else:
        exit()