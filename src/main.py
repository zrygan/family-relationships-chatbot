from imports import *
from rules import *

# initializing
prompt = Prompts()
family_tree = Family_Tree() 

# asks a query
def ask_question(input):
    names = prompt.extract_names(input) # extracting names
    relation, query = prompt.get_query(input, names)
 
    # FIXME: debugging

    """print("\nDebugging Query")
    print("Query: %s" % query)
    res = (list(family_tree.prolog.query(query)))
    print("Result: %s" % res)"""


    if query is not None:
        n = len(names)
        try:
            if "Is" in input:          
                result = bool(list(family_tree.prolog.query(query)))
                if result:
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
            return "I cannot say..."
    else:
        return "I am unable to comprehend your question..."

# adds fact to the knowledge base if valid
# returns the validity of the fact 
def handle_statement(input):
    # transform statement into an assertion
    statement = prompt.remove_vars_and_consts(input)
    names = prompt.extract_names(input)
    names = [name.lower() for name in names]
    assertions = prompt.get_assertion(input, names)

    # FIXME:
    """
    print("\nDebugging Statement")
    print("Assertion: %s" % assertions)
    """

    """
    if not prompt.is_predicate_valid(assertions): # check if predicate exists
        return "I am unable to comprehend your statement..."
    if prompt.is_redundant(assertion, family_tree.prolog): # check if assertion is already defined / already exists
            return "This is already known."
        elif not prompt.is_contradictory(assertion, family_tree.prolog): # check if assertion contradicts already defined facts
            return "This contradicts what is already known."
    """

    if not assertions:
        return "I am unable to comprehend your statement..."
    else:  # valid assertion
        try: 
            for assertion in assertions:
                family_tree.prolog.assertz(assertion)

                #FIXME:
                """
                print("\nDebugging Statement")
                print("Assertion: %s" % assertion)
                result = list(family_tree.prolog.query("siblings(ei, x)"))
                print("Result: %s" % result)
                """

            return "The AncesTree has absorbed knowledge!"
        except Exception as e:
            return "This statement is problematic."

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
            print("\n" + handle_statement(user_input))
        else: # invalid input
            print("\nYour message was confusing...")

if __name__ == "__main__":
    main()