from imports import *
from rules import *

# asks a query
def ask_question(input : str, f: Family_Tree):
    names = prompt.extract_names(input)
    relation, query = prompt.get_query(input, names)
    if query is not None:
        n = len(names)
        try:
            if "Is" in input:
                result = bool(list(Prolog.query(query)))
                if result:
                    return f"Yes, {names[0]} is {relation} of {names[1]}."
                else:
                    return f"No, {names[0]} is not {relation} of {names[1]}."
            elif "Are" in input:
                result = bool(list(Prolog.query(query)))
                if result:
                    if n == 4:
                        return (f"Yes, {names[0]}, {names[1]}, and {names[2]}"
                                f" are the {relation} of {names[3]}.")
                    elif n == 3:
                        return (f"Yes, {names[0]} and {names[1]}"
                                f" are the {relation} of {names[2]}.")
                    else:
                        return f"Yes, {names[0]} and {names[1]} are {relation}."
                else:
                    if n == 4:
                        return (f"No, {names[0]}, {names[1]}, and {names[2]}"
                                f" are not the {relation} of {names[3]}.")
                    elif n == 3:
                        return (f"No, {names[0]} and {names[1]}"
                                f" are not the {relation} of {names[2]}.")
                    else:
                        return f"No, {names[0]} and {names[1]} are not {relation}."
            else:
                people = list(Prolog.query(query))
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
def handle_statement(family_tree, user_input):
    prompts = Prompts()
    
    # transform statement into an assertion
    statement = prompts.remove_vars_and_consts(user_input)
    names = prompts.extract_names(user_input)
    assertions = prompts.get_assertion(user_input, names)
    """
    print("Statement: %s" % statement)
    print("Names: %s" % names)
    print("Assertions: %s" % assertions)
    """
    if True == True: # TODO: check validity of assertions here
        for assertion in assertions:
            family_tree.prolog.assertz(assertion)
    else:
        return False
    
    return True

def statement_testing():
    family_tree = Family_Tree()
    prompts = Prompts()

    statements = [
        "Finn and Jake are siblings.",
        "Fiona is a sister of Cake.",
        "Ei is the mother of Wanderer.",
        "Citlali is the grandmother of Ororon.",
        "Ash is a child of Delia.",
        "Marceline is a daughter of Hunson.",
        "IDontKnow is an uncle of Maybe.",
        "Lincoln is a brother of Leni.",
        "Norman is the father of Brendan.",
        "Marshal and Lily are parents of Marvin.",
        "Someone is a grandfather of somebody.",
        "Haley, Alex, Luke are children of Phil.",
        "Thor is a son of Odin.",
        "Claire is an aunt of Lily.",
    ]

    queries = [
        "siblings(Finn, Jake)",
        "sister(Fiona, Cake)",
        "mother(Ei, Wanderer)",
        "grandmother(Citlali, Ororon)",
        "child(Ash, Delia)",
        "daughter(Marceline, Hunson)",
        "uncle(IDontKnow, Maybe)",
        "brother(Lincoln, Leni)",
        "father(Norman, Brendan)",
        "parent(Lily, Marvin)",
        "grandfather(Someone, somebody)",
        "child(Phil, Luke)",
        "son(Thor, Odin)",
        "aunt(Claire, Lily)"
    ]

    test_name = [
        "siblings",
        "sister",
        "mother",
        "grandmother",
        "child",
        "daughter",
        "uncle",
        "brother",
        "father",
        "parents",
        "grandfather",
        "children",
        "son",
        "aunt"
    ]

    for i in range(0, len(queries)):
        print(f"\nTesting statement: {statements[i]}")
        handle_statement(family_tree, statements[i])

        results = list(prolog.query(queries[i]))
        try:
            if results:
                print(results)
            else:
                print("No results found.")
        except Exception as e:
            print(f"Error querying: {results}\n{e}")

def main():
    # print a welcome message for the user
    print("Greetings! I am the AncesTree!") 
    print("I house the knowledge that roots the connections of families.")

    # initializing
    family_tree = Family_Tree()
    prompt = Prompts()

    # loop chatbot
    while True:
        # prompt user for input 
        print("\nHow may I enlighten you today?")
        user_input = input("> ").strip() 

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nFarewell...")
            break

        if prompt.verify(user_input):
            # check if input is a question
            if user_input.endswith("?"):
                # ask PROLOG a query
                # print answer / YES / NO
                print(ask_question(user_input, family_tree))

                statement_testing()

            # check if input is a statement 
            elif user_input.endswith("."):
                # check with PROLOG if input is valid
                if handle_statement(family_tree, user_input) == True: # input is valid, added to the knowledge base
                    print("\nThe AncesTree has absorbed knowledge!")
                    
                    """
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
                    """

                else: # input is contradictory, invalid input
                    print("\nThe AncesTree deems information contradictory...")
            else:
                print("\nThe AncesTree is unable to comprehend your message...")

if __name__ == "__main__":
    main()