import time
import sys

def run_Game():
    '''Main function that runs the game'''


    def intro_text():
        """
        Function that runs a basic intruduction to the user.
        """ 

        print("\nHello!")
        print("In this quick game you will test your knowledge about house fire...")
        print("Will you be able to surive??")
        print("Are you ready??\n")

        user_choice = input("Y/N : \n")

        if user_choice.upper().strip() == "Y":
            clear_screen()
            print("Let's go!")
            time.sleep(1.5)
            first_question()
        elif user_choice.upper().strip() == "N":
            clear_screen()
            print("Come back when you are ready")
            time.sleep(1.5)
            intro_text()
        else:
            clear_screen()
            print("Type Y or N")
            time.sleep(1.5)
            intro_text()
        
    def first_question():
        pass

    def clear_screen():
        '''
        This function is used to clear the terminal
        Credit: https://stackoverflow.com/questions/63855637/clearing-the-terminal-for-my-python-text-adventure
        '''

        sys.stdout.write("\33[H\33[2J")
        sys.stdout.flush()

    intro_text()


run_Game()
