from imports import *

class Family_Tree:
    def __init__(self):
        self.prolog = Prolog()
        
        # the possible roles for every object
        self.roles = {
            1: "child",
            2: "daughter",
            3: "son",
            4: "siblings",
            5: "sister",
            6: "brother",
            7: "parents",
            8: "mother",
            9: "father",
            10: "aunt",
            11: "uncle",
            12: "grandparents",
            13: "grandmother",
            14: "grandfather",
            15: "relatives",
            16: "man",
            17: "woman" 
        }
        
        # a dictionary  of proerties of the object
        # the key is the name of the person (in lowercase)
        # the value is an array of properties (roles)
        # example of an entry: "Max" : [1,3,12] 
        #                      Max is a child, son, and a man
        # FIXME: idk if this is needed but it's here 
        self.objects = {}
        self.define_facts()
        
    def define_facts(self):
        # FIXME: comments are inconsistent, changed some rules here

         # X is a gparent        -> X is a parent of Y,  Y is a parent of Z
        self.prolog.assertz("grandparent(X,Z) :- child(Z,Y), child(Y,X)")

        # X is a gfather of Z   -> X is a gparent,      X is a man,             X is a parent of Y,         Y is a parent of Z
        self.prolog.assertz("grandfather(X,Z) :- man(X), grandparent(X,Z)")

        # X is a gmother of Z   -> X is a gparent,      X is a woman,           X is a parent of Y,         Y is a parent of Z
        self.prolog.assertz("grandmother(X,Z) :- woman(X), grandparent(X,Z)")



        # X is a child of Y     -> Y is a parent of X
        self.prolog.assertz("parent(X,Y) :- child(Y,X)")

        # X is a mother         -> X is a woman,        X is a parent of Y
        self.prolog.assertz("mother(X,Y) :- woman(X), child(Y,X)")

        # X is a father         -> X is a man,          X is a parent of Y
        self.prolog.assertz("father(X,Y) :- man(X), child(Y,X)")



        # X is an aunt of Z     -> X is a woman,        X, Y are siblings,      Y is a parent of Z
        self.prolog.assertz("aunt(X,Z) :- woman(X), siblings(X,Y), parent(Y,Z)")

        # X is an uncle of Z    -> X is a man,          X, Y are siblings,      Y is a parent of Z
        self.prolog.assertz("uncle(X,Z) :- man(X), siblings(X,Y), parent(Y,Z)")



        # X is a son of Y       -> X is a child of Y,   X is a man
        self.prolog.assertz("son(X,Y) :- child(X,Y), man(X)")

        # X is a daughter of Y  -> X is a child of Y,   Y is a woman
        self.prolog.assertz("daughter(X,Y) :- child(X,Y), woman(X)")



        # X and Y are siblings  -> X is a child of A,   Y is a child of A (X and Y are not the same person)
        self.prolog.assertz("siblings(X,Y) :- parent(A,X), parent(A,Y), X \\= Y")

        #
        self.prolog.assertz("sister(X,Y) :- siblings(X,Y), X \\= Y, woman(X)")

        # 
        self.prolog.assertz("brother(X,Y) :- siblings(X,Y), X \\= Y, man(X)")



        # X and Y are relatives -> X is a gfather of Y; Y is a gfather of X;    X is a parent of Y;         Y is a parent of X;
        #                          X is the aunt of Y;  Y is the aunt of X;     X is the uncle of Y;        Y is the uncle of X;
        #                          X and Y are siblings
        self.prolog.assertz(
            "relatives(X, Y) :- "
            "(grandparent(X, Y); grandparent(Y, X); "
            "grandmother(X, Y); grandmother(Y, X); "
            "grandfather(X, Y); grandfather(Y, X); "
            "parent(X, Y); parent(Y, X); "
            "mother(X, Y); mother(Y, X); "
            "father(X, Y); father(Y, X); "
            "aunt(X, Y); aunt(Y, X); "
            "uncle(X, Y); uncle(Y, X); "
            "daughter(X, Y); daughter(Y, X); "
            "son(X, Y); son(Y, X); "
            "sister(X, Y); sister(Y, X); "
            "brother(X, Y); brother(Y, X); "
            "siblings(X, Y); siblings(Y, X))"
        )
        
import re

class Prompts:
    def __init__(self):
        # a list of possible statement patterns
        self.statements = [
            "? and ? are siblings",
            "? is the sister of ?",
            "? is the mother of ?",
            "? is the child of ?",
            "? is the daughter of ?",
            "? is the brother of ?",
            "? and ? are the parents of ?",
            "? is the uncle of ?",
            "? is the father of ?",
            "? is a grandfather of ?",
            "? is a grandmother of ?",
            "?, ? and ? are the children of ?",
            "? is the son of ?",
            "? is the aunt of ?"
        ]
        
        # a list of possible question patterns
        self.questions = [
            "Are ? and ? siblings?",
            "Is ? a sister of ?",
            "Is ? a brother of ?",
            "Is ? the mother of ?",
            "Is ? the father of ?",
            "Are ? and ? the parents of ?",
            "Is ? a grandmother of ?",
            "Is ? a daughter of ?",
            "Is ? a son of ?",
            "Is ? a child of ?",
            "Are ? ? and ? children of ?",
            "Is ? an uncle of ?",
            "Who are the siblings of ?",
            "Who are the sisters of ?",
            "Who are the brothers of ?",
            "Who is the mother of ?",
            "Who is the father of ?",
            "Who are the parents of ?",
            "Is ? a grandfather of ?",
            "Who are the daughters of ?",
            "Who are the sons of ?",
            "Who are the children of ?",
            "Is ? an aunt of ?",
            "Are ? and ? relatives?"
        ]
        
        # set of words that cannot be replaced with '?'
        self.allowed_words = set(self.extract_keywords(self.questions))

    def verify(self, string):
        """checks if the string is a possible statement or question
        Remark. to use this, the string must be handled already,
               that is, the variables or constants in the statement or question
               are replaced with the ?        
        Args:
            string (str): the string 
        Returns:
            bool: (true) if string is in questions or statements, otherwise false
        """
        # Normalize the string by replacing variables with '?'
        transformed_string = self.remove_vars_and_consts(string)
        
        # Check if the transformed string matches any predefined pattern
        return any(transformed_string == pattern for pattern in self.questions + self.statements)
    
    def extract_keywords(self, questions):
        """
        Extract keywords from the list of questions.
        This includes all words that should not be changed to ?.
        """
        keywords = set()
        for question in questions:
            words = re.findall(r'\w+', question.lower())
            keywords.update(words)
        return keywords
    
    def remove_vars_and_consts(self, string: str) -> str:
        """Replace all names and other words not in the predefined list with '?'.
        Args:
            string (str): The input sentence containing names and relationships.
        Returns:
            str: A transformed version of the string where unknown words are replaced with '?'.
        """
        words = string.split()
        
        transformed_words = []
        
        for word in words:
            cleaned_word = re.sub(r'\W+', '', word).lower()
            
            if cleaned_word in self.allowed_words:
                transformed_words.append(word)
            else:
                transformed_words.append('?')
        
        return ' '.join(transformed_words)

    def extract_names(self, string: str):
        string = string.split()
        names = []
        for word in string:
            cleaned_word = re.sub(r'\W+', '', word).lower()
            if cleaned_word not in self.allowed_words:
                if "?" in word or "." in word or "," in word:
                    word = word[:-1]
                names.append(word)
        return names
    
    def get_query(self, string: str, names):
        names = [name.lower() for name in names]
        if "Who" in string:
            if "are the daughters of" in string:
                return "daughters", f"daughter(X, {names[0]})"
            elif "are the sons of" in string:
                return "sons", f"son(X, {names[0]})"
            elif "are the children of" in string:
                return "children", f"child(X, {names[0]})"
            elif "are the siblings of" in string:
                return "siblings", f"siblings(X, {names[0]})"
            elif "are the sisters of" in string:
                return "sisters", f"siblings(X, {names[0]}), woman(X)"
            elif "are the brothers of" in string:
                return "brothers", f"siblings(X, {names[0]}), man(X)"
            elif "is the mother of" in string:
                return "mother", f"parent(X, {names[0]}), woman(X)"
            elif "is the father of" in string:
                return "father", f"parent(X, {names[0]}), man(X)"
            elif "are the parents of" in string:
                return "parents", f"parent(X, {names[0]})"
        else:
            if "Is" in string:
                if "a sister of" in string:
                    return "a sister", f"siblings({names[0]}, {names[1]}), woman({names[0]})"
                elif "a brother of" in string:
                    return "a brother", f"siblings({names[0]}, {names[1]}), man({names[0]})"
                elif "the mother of" in string:
                    return "the mother", f"parent({names[0]}, {names[1]}), woman({names[0]})"
                elif "the father of" in string:
                    return "the father", f"parent({names[0]}, {names[1]}), man({names[0]})"
                elif "a grandmother of" in string:
                    return "a grandmother", f"grandmother({names[0]}, {names[1]})"
                elif "a daughter of" in string:
                    return "a daughter", f"daughter({names[0]}, {names[1]})"
                elif "a son of" in string:
                    return "a son", f"son({names[0]}, {names[1]})"
                elif "a child of" in string:
                    return "a child", f"child({names[0]}, {names[1]})"
                elif "an uncle of" in string:
                    return "an uncle", f"uncle({names[0]}, {names[1]})"
                elif "a grandfather of" in string:
                    return "a grandfather",f"grandfather({names[0]}, {names[1]})"
                elif "an aunt of" in string:
                    return "an aunt",f"aunt({names[0]}, {names[1]})"
            elif "Are" in string:
                n = len(names)
                if n > 3:
                    if "children of" in string:
                        query = ""
                        for i in range(n - 1):
                            if i < n - 2:
                                query += f"child({names[i]}, {names[n-1]}), "
                            else:
                                query += f"child({names[i]}, {names[n-1]})"
                        return "children", query
                elif n == 3:
                    if "the parents of" in string:
                        return "parents",f"parent({names[0]}, {names[2]}), parent({names[1]}, {names[2]})"
                    elif "children of" in string:
                        return "children",f"child({names[0]}, {names[2]}), child({names[1]}, {names[2]})"
                else:
                    if "siblings" in string:
                        return "siblings",f"siblings({names[0]}, {names[1]})"
                    elif "relatives" in string:
                        return "relatives",f"relatives({names[0]}, {names[1]})"
        return None, None

    def get_assertion(self, statement, names):
        assertions = []

        # grandparents
        if "is a grandfather of" in statement:
            assertions = [f"child(X, {names[0]})",
                          f"child({names[1]}, X)",
                          f"man({names[0]})"]
        elif "is a grandmother of" in statement:
            assertions = [f"child(X, {names[0]})",
                          f"child({names[1]}, X)",
                          f"woman({names[0]})"]
        elif "is a grandparent of" in statement:
            assertions = [f"child(X, {names[0]})",
                          f"child({names[1]}, X)"]

        # parents
        elif "is the mother of" in statement:
            assertions = [f"woman({names[0]})",
                          f"child({names[1]}, {names[0]})"]
        elif "is the father of" in statement:
            assertions = [f"man({names[0]})",
                          f"child({names[1]}, {names[0]})"]
        elif "and" in statement and "are the parents of" in statement:
            assertions = [f"child({names[2]}, {names[0]})",
                          f"child({names[2]}, {names[1]})"]

        # aunt and uncle
        elif "is an aunt of" in statement:
            assertions = [f"woman({names[0]})",
                          f"child({names[0]}, A)",
                          f"child(Y, A)",
                          f"child({names[1]}, Y)"]
        elif "is an uncle of" in statement:
            assertions = [f"man({names[0]})",
                          f"child({names[0]}, A)",
                          f"child(Y, A)",
                          f"child({names[1]}, Y)"]

        # children
        elif "is a child of" in statement:
            assertions = [f"child({names[0]}, {names[1]})"]
        elif "and" in statement and "are children of" in statement:
            for i in range(len(names) - 1):
                assertions.append(f"child({names[i]}, {names[-1]})")
        elif "is a son of" in statement:
            assertions = [f"man({names[0]})",
                          f"child({names[1]}, {names[0]})"]
        elif "is a daughter of" in statement:
            assertions = [f"woman({names[0]})",
                          f"child({names[1]}, {names[0]})"]

        # siblings
        elif "and" in statement and "are siblings" in statement:
            assertions = [f"child({names[0]}, A)",
                          f"child({names[1]}, A)"]
        elif "is a brother of" in statement:
            assertions = [f"man({names[0]})",
                          f"child({names[0]}, A)",
                          f"child({names[1]}, A)"]
        elif "is a sister of" in statement:
            assertions = [f"woman({names[0]})",
                          f"child({names[0]}, A)",
                          f"child({names[1]}, A)"]

        return assertions
    
    # TODO:
    def is_assertion_valid(self, assertion, prolog):
        return True