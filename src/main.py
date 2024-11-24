from imports import *
from rules import *

from src.rules import Prompts
# TODO: implement this method
# initializes PROLOG
# def initialize_prolog(): 

# TODO: implement this method
# initializes rules
# def initialize_rules():

# TODO: implement this method
# asks a query
def ask_question(input : str, f: Family_Tree):
    names = prompt.extract_names(input)
    query = prompt.get_query(input, names)
    print(query)
    if query != None:
        print("lol")
        result = f.prolog.query(query)
        print("lol")

        """for soln in result:
            print(soln)"""
        return "WIP"
    else:
        return "I don't know."

# TODO: implement this method
# adds a fact to the knowledge base
# def handle_statement():

prompt = Prompts()

def main():
    # print a welcome message for the user FIXME: placeholder / also this is extremely optional
    print("Greetings! I'm the AncesTree!") # this is so adorable HAHAHAH (zry)
    print("I house the knowledge that roots your family's connections.")
    print("How may I enlighten you today?")

    # initializing 
    family_tree = Family_Tree()

    # loop chatbot
    while True:
        # prompt user for input 
        user_input = input("> ").strip() 

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nFarewell...")
            break

        #user_input = "Ei is a sister of Makoto." # FIXME: for testing only

        # FIXME: (if the input contains a question mark according to the specs)
        # check if input is a question 
        # check if input is a question FIXME: (if the input contains a question mark according to the specs)
        if prompt.verify(user_input):
            # check if input is a question FIXME: (if the input contains a question mark according to the specs)
            if "?" in user_input:
                # ask PROLOG a query
                # print answer / YES / NO
                print(ask_question(user_input, family_tree))

            # check if input is a statement (most likely ends with a period)
            elif "." in user_input:

                # check with PROLOG if input is feasible
                pass

                    # if YES, add to PROLOG knowledge base

                        # print prompt that chatbot learned a fact

                    # if NO, print an error message

if __name__ == "__main__":
    main()