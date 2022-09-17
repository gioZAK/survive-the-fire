import time
import sys
import random
from quotes import *

POSITIVE = ["Good Job!", "Great!", "You are correct!", "😃"]
NEGATIVE = ["Oh no!!!", "Try Again", "That's incorrect", "😔"]

def run_game():
    '''Main function that runs the game'''

    print("Loading...")
    time.sleep(0.5)
    

    def intro_text():
        """
        Function that runs a basic intruduction to the user.
        """ 
        clear_screen()
        print("\nHello!")
        print("In this quick game you will test your knowledge about house fire...")
        print("Will you be able to surive??")
        print("Are you ready??\n")

        user_choice = input("Y/N : \n")

        if user_choice.upper().strip() == "Y":
            clear_screen()
            print("Let's go!")
            time.sleep(2)
            first_question()
        elif user_choice.upper().strip() == "N":
            clear_screen()
            print("Come back when you are ready")
            time.sleep(2)
            intro_text()
        else:
            clear_screen()
            print("Type Y or N")
            time.sleep(2)
            intro_text()
        
    def first_question():
        clear_screen()
        print("You smell smoke, but no one else is reacting. You should:\n")
        print("A: Alert others of your concern and go outside right away.")
        print("B: Do nothing. Since nobody else is reacting, why should you.")
        print("C: Wait for instructions.")

        time.sleep(1)

        user_choice1 = input("A - B - C: \n")

        if user_choice1.upper().strip() == "A":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_1()
            time.sleep(1.5)
            second_question()
        elif user_choice1.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_1()
            time.sleep(1.5)
            first_question()
        elif user_choice1.upper().strip() == "C":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_1()
            time.sleep(1.5)
            first_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(1.5)
            first_question()

    def second_question():
        pass


    def clear_screen():
        '''
        This function is used to clear the terminal
        Credit: https://stackoverflow.com/questions/63855637/clearing-the-terminal-for-my-python-text-adventure
        '''

        sys.stdout.write("\33[H\33[2J")
        sys.stdout.flush()

    intro_text()


run_game()
