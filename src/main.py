from imports import *
from rules import *

# initializing
prompt = Prompts()
family_tree = Family_Tree() 

# asks a query
def ask_question(input):
    names = prompt.extract_names(input) # extracting names
    relation, query = prompt.get_query(input, names)

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
            return "Sorry. I cannot say..."
    else:
        return "My apologies. Your question confuses me."

# adds fact to the knowledge base if valid
# returns the validity of the fact 
def handle_statement(input):
    try: # transform statement into an assertion
        statement = prompt.remove_vars_and_consts(input)
        names = prompt.extract_names(input)
        names = [name.lower() for name in names]
        query, assertions = prompt.get_assertion(input, names, family_tree)
    except Exception as e: # name/s caused errors
        return "Who were you talking about again?"

    if not assertions: # assertion was not generated
        return "Your statement confuses me. Can you say that again?"
    
    if not prompt.is_assertion_feasible(statement, names, family_tree): # checks if dependent facts can be proven ( grandparents / aunts / uncles/ siblings )
        return "Hmm... We cannot say for sure..."

    if prompt.assertion_exists(query[0], family_tree):
        return "Oh! I already know this."

    for q in query: # checking validity of assertions
        if not prompt.is_assertion_valid(q, names, family_tree):
            return "I don't think that's possible..."
        
    try: # valid assertion
        for assertion in assertions:
            # print("asserted: " + assertion + "!")
            family_tree.prolog.assertz(assertion)
        return "Alright! I've grasped this knowledge"
    except Exception as e:
        return "Hmmm... Your statement is problematic."

def main():
    os.system('cls')
    # print a welcome message for the user
    print("Greetings! I am the AncesTree.") 
    #time.sleep(1)
    print("I house knowledge which unites families!")
    #time.sleep(1)
    print("Ask me a question or supply me with information.")
    #time.sleep(1)

    # array of messages
    messages = [
        "I be-leaf in you.",
        "Always here to help.",
        "Go on, enlighten me.",
        "How are you? I'm Oak-ay!",
        "Do you have any questions?",
        "Leave no branch unexplored.",
        "Look at you, all spruced up.",
        "Your knowledge helps me grow!",
        "Who wood you like to know about?",
        "Tell me more about your family tree.",
    ]

    # loop chatbot
    while True:
        # prompt user for input 
        print("\n" + random.choice(messages))
        user_input = input("> ").strip() 

        # exiting chatbot
        if user_input.lower() == "exit":
            print("\nI'm rooting for you! Farewell...")

        # checking input
        if user_input.endswith("?"): # check if input is a question
            print("\n" + ask_question(user_input)) # getting an answer
        elif user_input.endswith("."): # check if input is a statement 
            print("\n" + handle_statement(user_input))
        else: # invalid input
            print("\nI'm stumped! I couldn't understand.")

if __name__ == "__main__":
    main()