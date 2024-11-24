from imports import *
from rules import *

# TODO: implement this method
# asks a query
# def ask_question():

# adds fact to the knowledge base if valid
# returns the validity of the fact 
def handle_statement(family_tree, user_input):
    prompts = Prompts()
    
    # transform statement into an assertion
    statement = prompts.remove_vars_and_consts(user_input)
    names = prompts.extract_names(user_input)
    assertions = prompts.get_assertion(user_input, names)

    print("Statement: %s" % statement)
    print("Names: %s" % names)
    print("Assertions: %s" % assertions)

    if True == True: # TODO: check validity of assertions here
        for assertion in assertions:
            family_tree.prolog.assertz(assertion)
    else:
        return False
    
    return True

def main():
    # print a welcome message for the user
    print("Greetings! I am the AncesTree!") 
    print("I house the knowledge that roots the connections of families.")

    # initializing 
    family_tree = Family_Tree()
    prompts = Prompts()

    # loop chatbot
    while True:
        # prompt user for input 
        print("\nHow may I enlighten you today?")
        user_input = input("> ").strip() 
        query_input = input("> ").strip() 

        #FIXME: test
        user_input = "Lyney and Lynette are siblings."
        query_input = "siblings(Lyney, X)"

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nFarewell...")
            break









        # FIXME: (if the input contains a question mark according to the specs)
        # check if input is a question 
        if prompts.verify(user_input):
            names = prompts.extract_names(user_input)
            # print(names) //for debugging

        # ask PROLOG a query

        # print answer / YES / NO
            # check if input is a question FIXME: (if the input contains a question mark according to the specs)
            if "?" in user_input:
                # ask PROLOG a query
                pass
                # print answer / YES / NO






        # check if input is a statement 
        elif user_input.endswith("."):
            # check with PROLOG if input is valid
            if handle_statement(family_tree, user_input) == True: # input is valid, added to the knowledge base
                print("\nThe AncesTree has absorbed knowledge!")
                
                #FIXME: testing
                print("\nQuerying")
                try:
                    results = list(prolog.query(query_input))
                    if results:
                        print(results)
                    else:
                        print("No results found.")
                except Exception as e:
                    print(f"Error querying: {query_input}\n{e}")

            else: # input is contradictory, invalid input
                print("\nThe AncesTree deems information contradictory...")
        else:
            print("\nThe AncesTree is unable to comprehend your message...")

if __name__ == "__main__":
    main()