from imports import *
from src.rules import Prompts
# TODO: implement this method
# initializes PROLOG
# def initialize_prolog(): 

# TODO: implement this method
# initializes rules
# def initialize_rules():

# TODO: implement this method
# asks a query
# def ask_question():

# TODO: implement this method
# adds a fact to the knowledge base
# def handle_statement():

prompt = Prompts()

def main():
    # print a welcome message for the user FIXME: placeholder / also this is extremely optional
    print("Greetings! I'm the AncesTree!") # this is so adorable HAHAHAH (zry)
    print("I house the knowledge that roots your family's connections.")
    print("How may I enlighten you today?")

    # loop program FIXME: specs say it should loop but never when it terminates
    while True:
        # prompt user for input 
        user_input = input("> ").strip()

        # check if input is a question FIXME: (if the input contains a question mark according to the specs)
        if prompt.verify(user_input):
            names = prompt.extract_names(user_input)
            # print(names) //for debugging

            # check if input is a question FIXME: (if the input contains a question mark according to the specs)
            if "?" in user_input:
                # ask PROLOG a query
                pass
                # print answer / YES / NO

            # check if input is a statement (most likely ends with a period)
            elif "." in user_input:
                # check with PROLOG if input is feasible
                pass
                # if YES, add to PROLOG knowledge base

                # print prompt that chatbot learned a fact

                # if NO, print an error message

if __name__ == "__main__":
    main()