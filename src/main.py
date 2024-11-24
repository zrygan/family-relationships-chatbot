from imports import *
from rules import *

# TODO: implement this method
# asks a query
# def ask_question():

# adds fact to the knowledge base if valid
# returns the validity of the fact 
def handle_statement(family_tree, user_input, query):
    prompts = Prompts()
    
    # transform statement into an assertion
    statement = prompts.remove_vars_and_consts(user_input) # getting the kind of statement (ex. "? is a sister of ?")
    names = prompts.extract_names(user_input) # getting the names involved (ex. ["Ei", "Makoto"])
    assertions = prompts.get_assertion(statement, names) # formatting the statement as PROLOG assertions

    print("\nAssertion:") # FIXME: testing only
    print(assertions) # FIXME: testing only
    print("\nQuery: \n" + query + "\n") # FIXME: testing only

    # check with PROLOG if input is feasible TODO: ask query here !
    if 1 == True: #FIXME: implement ask query here !
        # add to knowledge base # TODO: 
        for assertion in assertions:
            family_tree.prolog.assertz(assertion)
            result = family_tree.prolog.query(query)
            for solution in result:
                print(solution)
        return True
    else:
        return False

def main():
    # print a welcome message for the user FIXME: placeholder / also this is extremely optional
    print("Greetings! I'm the AncesTree!") # this is so adorable HAHAHAH (zry)
    print("I house the knowledge that roots your family's connections.")

    # initializing 
    family_tree = Family_Tree()
    prompts = Prompts()

    # loop chatbot
    while True:
        # prompt user for input 
        print("\nHow may I enlighten you today?")
        # user_input = input("> ").strip() 
        query_input = input("> ").strip() 

        user_input = "Ei and Makoto are siblings."
        query_input = "siblings(Makoto, X)"

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nFarewell...")
            break

        # user_input = "Ei and Makoto are siblings." # FIXME: for testing only









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
            if handle_statement(family_tree, user_input, query_input) == True: # input is valid, added to the knowledge base
                print("\nThe AncesTree has absorbed knowledge!")
            else: # input is contradictory, invalid input
                print("\nThe AncesTree deems information contradictory...")
        else:
            print("\nThe AncesTree is unable to comprehend your message...")

if __name__ == "__main__":
    main()