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
            if user_input.endswith("?"):
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
