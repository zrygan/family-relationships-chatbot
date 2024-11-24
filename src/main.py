from imports import *
from rules import *

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

def main():
    # print a welcome message for the user FIXME: placeholder / also this is extremely optional
    print("Greetings! I'm the AncesTree!") # this is so adorable HAHAHAH (zry)
    print("I house the knowledge that roots your family's connections.")
    print("How may I enlighten you today?")

    # initializing 
    family_tree = Family_Tree()
    prompts = Prompts()

    # loop chatbot
    while True:
        # prompt user for input 
        # user_input = input("> ").strip()
        user_input = "Ei is a sister of Makoto"


        # FIXME: (if the input contains a question mark according to the specs)
        # check if input is a question 

        # ask PROLOG a query

        # print answer / YES / NO






        # FIXME:
        # check if input is a statement (most likely ends with a period)
        if user_input.endswith("."):
            # handle statement
            family_tree.add_fact(user_input)
            print(prompts.learned_fact_prompt)
        # check with PROLOG if input is feasible 

        # if YES, add to PROLOG knowledge base

        # print prompt that chatbot learned a fact

        # if NO, print an error message

if __name__ == "__main__":
    main()