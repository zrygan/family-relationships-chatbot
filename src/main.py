from imports import *
from rules import *

# asks a query
def ask_question(input):
    names = prompt.extract_names(input)
    relation, query = prompt.get_query(input, names)

    if query is not None:
        n = len(names)
        try:
            if "Is" in input:          
                result = bool(list(family_tree.prolog.query(query)))
                if result:
                    print("yo")
                    return f"Yes, {names[0]} is {relation} of {names[1]}."
                else:
                    return f"No, {names[0]} is not {relation} of {names[1]}."
            elif "Are" in input:
                result = bool(list(family_tree.prolog.query(query)))
                if result:
                    if n > 3:
                        response = "Yes, "
                        for i in range(n-1):
                            if i < n - 2:
                                response += f"{names[i]}, "
                            else:
                                response += f"and {names[i]}"
                        response += f" are the {relation} of {names[n-1]}."
                        return response
                    elif n == 3:
                        if "children" in input:
                            return (f"Yes, {names[0]} and {names[1]}"
                                    f" are {relation} of {names[2]}.")
                        return (f"Yes, {names[0]} and {names[1]}"
                                f" are the {relation} of {names[2]}.")
                    else:
                        return f"Yes, {names[0]} and {names[1]} are {relation}."
                else:
                    if n > 3:
                        response = "No, "
                        for i in range(n - 1):
                            if i < n - 2:
                                response += f"{names[i]}, "
                            else:
                                response += f"and {names[i]}"
                        response += f" are not the {relation} of {names[n - 1]}."
                        return response
                    elif n == 3:
                        if "children" in input:
                            return (f"No, {names[0]} and {names[1]}"
                                    f" are not {relation} of {names[2]}.")
                        return (f"No, {names[0]} and {names[1]}"
                                f" are not the {relation} of {names[2]}.")
                    else:
                        return f"No, {names[0]} and {names[1]} are not {relation}."
            else:
                people = list(family_tree.prolog.query(query))
                ppl_set = {person['X'].capitalize() for person in people}
                people = list(ppl_set)
                result = ""
                n = len(people)
                if n > 2:
                    for i in range(n):
                        if i < n - 1:
                            result += f"{people[i]}, "
                        else:
                            result += f"and {people[i]}"
                    result += f" are the {relation} of {names[0]}."
                elif n == 2:
                    result += f"{people[0]} and {people[1]} are the {relation} of {names[0]}."
                elif n == 1:
                    if relation.endswith("s"):
                        relation = relation[:-1]
                    elif relation == "children":
                        relation = "child"
                    result += f"{people[0]} is the {relation} of {names[0]}."
                else:
                    result += f"{names[0]} has no {relation}."
                return result
        except Exception as e:
            return "I don't know."
    else:
        return "I don't understand your question."

# adds fact to the knowledge base if valid
# returns the validity of the fact 
def handle_statement(user_input):
    # transform statement into an assertion
    statement = prompt.remove_vars_and_consts(user_input)
    names = prompt.extract_names(user_input)
    assertions = prompt.get_assertion(user_input, names)

    if True == True: # TODO: check validity of assertions here
        for assertion in assertions:
            family_tree.prolog.assertz(assertion)
    else:
        return False
    return True

# initializing
prompt = Prompts()
family_tree = Family_Tree()

family_tree.prolog.assertz("parent(bob, bandit)")
family_tree.prolog.assertz("parent(bob, radley)")
family_tree.prolog.assertz("parent(bob, stripe)")
family_tree.prolog.assertz("parent(chris, bandit)")
family_tree.prolog.assertz("parent(chris, radley)")
family_tree.prolog.assertz("parent(chris, stripe)")

family_tree.prolog.assertz("parent(bandit, bluey)")
family_tree.prolog.assertz("parent(bandit, bingo)")
family_tree.prolog.assertz("parent(chilli, bluey)")
family_tree.prolog.assertz("parent(chilli, bingo)")

family_tree.prolog.assertz("parent(stripe, muffin)")
family_tree.prolog.assertz("parent(stripe, socks)")
family_tree.prolog.assertz("parent(trixie, muffin)")
family_tree.prolog.assertz("parent(trixie, socks)")

family_tree.prolog.assertz("parent(mort, brandy)")
family_tree.prolog.assertz("parent(mort, chilli)")


family_tree.prolog.assertz("man(bob)")
family_tree.prolog.assertz("man(radley)")
family_tree.prolog.assertz("man(bandit)")
family_tree.prolog.assertz("man(stripe)")
family_tree.prolog.assertz("man(mort)")

family_tree.prolog.assertz("woman(bluey)")
family_tree.prolog.assertz("woman(bingo)")
family_tree.prolog.assertz("woman(muffin)")
family_tree.prolog.assertz("woman(socks)")
family_tree.prolog.assertz("woman(brandy)")
family_tree.prolog.assertz("woman(chilli)")
family_tree.prolog.assertz("woman(chris)")
family_tree.prolog.assertz("woman(trixie)")


def main():
    # print a welcome message for the user
    print("Greetings! I am the AncesTree!") 
    print("I house the knowledge that roots the connections of families.")

    # loop chatbot
    while True:
        # prompt user for input 
        print("\nHow may I enlighten you today?")
        user_input = input("> ").strip() 

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nFarewell...")
            break

        # checking input
        if user_input.endswith("?"): # check if input is a question
            print("\n" + ask_question(user_input)) # getting an answer
        elif user_input.endswith("."): # check if input is a statement 
            # check with PROLOG if input is valid
            if handle_statement(user_input) == True: # input is valid, added to the knowledge base
                print("\nThe AncesTree has absorbed knowledge!")
            else: # input is contradictory, invalid input
                print("\nThe AncesTree deems information contradictory...")
        else: # invalid input
            print("\nThe AncesTree is unable to comprehend your message...")

if __name__ == "__main__":
    main()