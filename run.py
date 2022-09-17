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

        print("Hello!\n")
        print("In this game you will test your knowledge about house fire!")
        print("Will you be able to surive??\n")
        print("Are you ready??\n")

        user_choice = input("Type: Y/N : \n")

        if user_choice.upper().strip() == "Y":
            clear_screen()
            print("Let's go!")
            time.sleep(1)
            first_question()
        elif user_choice.upper().strip() == "N":
            clear_screen()
            print("Come back when you are ready")
            time.sleep(1)
            intro_text()
        else:
            clear_screen()
            print("Type Y or N")
            time.sleep(1.5)
            intro_text()

    def first_question():
        clear_screen()

        print("You smell smoke, but no one else is reacting. You should:\n")
        print("A: Alert others of your concern and go outside right away.\n")
        print("B: Do nothing. Since nobody else is reacting.\n")
        print("C: Wait for instructions.\n")

        time.sleep(1)

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_1()
            time.sleep(3)
            second_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_1()
            time.sleep(3)
            first_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_1()
            time.sleep(3)
            first_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            first_question()

    def second_question():
        clear_screen()

        print("You're in your bedroom and you hear a smoke alarm.")
        print("You Should: \n")
        print("A: Disable it. If you don't smell smoke or see flames,")
        print("then everything is OK.\n")
        print("B: Feel the handle to your closed door with the back of")
        print("your hand. Open it Slowly and make your way outside.\n")
        print("C: Run outside right away.\n")

        time.sleep(1)

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_2()
            time.sleep(3)
            second_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_2()
            time.sleep(3)
            third_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_2()
            time.sleep(3)
            second_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            second_question()

    def third_question():
        clear_screen()

        print("You see a small fire, and you have an appropriate")
        print("fire extinguisher close at hand. You should:\n")
        print("A: Use the fire extinguisher,")
        print("and get out if it doesn't immediately put out the fire.\n")
        print("B: Have everyone else stay put while")
        print("you try to extinguish the fire.\n")
        print("C: Dump water on the fire first, and then use the fire")
        print("extinguisher. Eventually the flames will subside.\n")

        time.sleep(1)

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_3()
            time.sleep(3)
            fourth_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_3()
            time.sleep(3)
            third_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_3()
            time.sleep(3)
            third_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            third_question()

    def fourth_question():
        clear_screen()

        print("There's a fire, but your escape route is clear.")
        print("While you exit the burning building, you should:\n")
        print("A: Grab your belongings before leaving.\n ")
        print("B: Open windows as you go to make it")
        print("easier for firefighters to get inside.\n")
        print("C: Close doors and windows behind you when you can.\n")

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_4()
            time.sleep(3)
            fourth_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_4()
            time.sleep(3)
            fourth_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_4()
            time.sleep(3)
            fifth_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            fourth_question()

    def fifth_question():
        clear_screen()

        print("As you are making your way out of the building,")
        print("your clothes catch fire. You should:\n")
        print("A: Keep going and deal with it once you're outside.\n")
        print("B: Pat out the flames while you go.\n")
        print("C: Stop, drop and roll.\n")

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_5()
            time.sleep(3)
            fifth_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_5()
            time.sleep(3)
            fifth_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_5()
            time.sleep(3)
            sixth_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            fifth_question()

    def sixth_question():
        clear_screen()

        print("Your escape route is filled with heavy smoke. You should:\n")
        print("A: Find a different way out.\n")
        print("B: Go anyway. Just move quickly.\n")
        print("C: Stay put and wait for help.\n")

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_6()
            time.sleep(3)
            seventh_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_6()
            time.sleep(3)
            sixth_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_6()
            time.sleep(3)
            sixth_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            sixth_question()

    def seventh_question():
        clear_screen()

        print("All escape routes are blocked. You should:\n")
        print("A: Go anyway. Run through the blockage")
        print("to make your way to safety.\n")
        print("B: Hide in a closet or under a bed.\n")
        print("C: Close the door and block all cracks and")
        print("vents with tape or a damp cloth.\n")

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_7()
            time.sleep(3)
            seventh_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_7()
            time.sleep(3)
            seventh_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_7()
            time.sleep(3)
            eight_question()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            seventh_question()

    def eight_question():
        clear_screen()

        print("You've made it! You safely got out of the building,")
        print("and the fire doesn't look that bad. You should:\n")
        print("A: Go back inside to grab your cell phone.\n")
        print("B: Go inside, grab a fire extinguisher,")
        print("and try to fight the flames\n")
        print("C: Stay outside and head to your.")
        print("identified meeting place\n")

        user_choice = input("Type: A - B - C: \n")

        if user_choice.upper().strip() == "A":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_8()
            time.sleep(3)
            eight_question()
        elif user_choice.upper().strip() == "B":
            clear_screen()
            print(random.choice(NEGATIVE))
            quotes_8()
            time.sleep(3)
            eight_question()
        elif user_choice.upper().strip() == "C":
            clear_screen()
            print(random.choice(POSITIVE))
            quotes_8()
            time.sleep(3)
            end_game()
        else:
            clear_screen()
            print("Type A, B or C.")
            time.sleep(3)
            eight_question()

    def end_game():
        clear_screen()

        print("Congratulations!!!\n")
        print("You have finished the quiz!")
        print("Hopefully you will never have to use this knowledge.")
        print("Remember: Prevention is your best bet!")
        print("Thank you and stay safe!")

        print("\nType anything and press enter to play again")
        user_choice = input("Type: ")
        if user_choice is False:
            pass
        else:
            intro_text()

    def clear_screen():
        '''
        This function is used to clear the terminal
        Source: "https://stackoverflow.com/questions/63855637/
        clearing-the-terminal-for-my-python-text-adventure"
        '''

        sys.stdout.write("\33[H\33[2J")
        sys.stdout.flush()

    intro_text()


run_game()
