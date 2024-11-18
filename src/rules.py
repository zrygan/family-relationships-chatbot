from imports import *

class Family_Tree:
    def __init__(self):
        self.prolog = Prolog()
        # the possible roles for every object
        self.roles = {
            1: "child",
            2: "daugher",
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
        self.objects = {}
        self.define_facts()
        
    def define_facts(self):
        # X is a child of Y     -> Y is a parent of X
        self.prolog.assertz("child(X,Y) :- parent(Y,X)")
        
        # X and Y are siblings  -> X is a child of A,   Y is a child of A (X and Y are not the same person)
        self.prolog.assertz("siblings(X,Y) :- child(X,A), child(Y,A), X\\=Y")
        
        # X is a son of Y       -> X is a child of Y,   X is a man
        self.prolog.assertz("son(X,Y) :- child(X,Y), man(X)")
        
        # X is a daughter of Y  -> X is a child of Y,   Y is a woman
        self.prolog.assertz("daugher(X,Y) :- child(X,Y), woman(X)")
        
        # X is a mother         -> X is a woman,        X is a parent of Y
        self.prolog.assertz("mother(X) :- woman(X), parent(X,Y)")
        
        # X is a mother         -> X is a woman,        Y is a child of X
        self.prolog.assertz("mother(X) :- woman(X), child(Y,X)")
        
        # X is a father         -> X is a man,          X is a parent of Y
        self.prolog.assertz("father(X) :- man(X), parent(X,Y)")
        
        # X is a father         -> X is a man,          Y is a child of X
        self.prolog.assertz("father(X) :- man(X), child(Y,X)")
        
        # X is a parent of Y    -> Y is a child of X
        self.prolog.assertz("parent(X,Y) :- child(Y,X)")
        
        # X is a gparent        -> X is a parent of Y,  Y is a parent of Z
        self.prolog.assertz("grandparent(X) :- parent(X,Y), parent(Y,Z)")
        
        # X is a gfather of Z   -> X is a gparent,      X is a man,             X is a parent of Y,         Y is a parent of Z
        self.prolog.assertz("grandfather(X,Z) -: grandparent(X), man(X), parent(X,Y), parent(Y,Z)")
        
        # X is a gmother of Z   -> X is a gparent,      X is a woman,           X is a parent of Y,         Y is a parent of Z
        self.prolog.assertz("grandmother(X,Z) -: grandparent(X), woman(X), parent(X,Y), parent(Y,Z)")
        
        # X is an aunt of Z     -> X is a woman,        X, Y are siblings,      Y is a parent of Z
        self.prolog.assertz("aunt(X,Z) -: woman(X), siblings(X,Y), parent(Y,Z)")
        
        # X is an uncle of Z    -> X is a man,          X, Y are siblings,      Y is a parent of Z
        self.prolog.assertz("uncle(X,Z) -: man(X), siblings(X,Y), parent(Y,Z)")
        
        # X and Y are relatives -> X is a gfather of Y; Y is a gfather of X;    X is a parent of Y;         Y is a parent of X;
        #                          X is the aunt of Y;  Y is the aunt of X;     X is the uncle of Y;        Y is the uncle of X;
        #                          X and Y are siblings
        self.prolog.assertz("relatives(X,Y) -: grandfather(X,Y); grandfather(Y,X); parent(X,Y); parent(Y,X); aunt(X,Y); aunt(Y,X); uncle(X,Y); uncle(Y,X); siblings(X,Y)")      


class Prompts:
    def __init__(self):
        # a list of possible statement patterns
        # each pattern has ? to indicate the blanks in the sentence pattern
        # for simplicity no punctuation
        # TODO: can you help me, double check if this is complete
        #       if it is, you can delete this thanks (zry)
        self.statements = [
                        "? and ? are siblings",
                        "? is the sister of ?",
                        "? is the mother of ?",
                        "? is the child of ?",
                        "? is the daugher of ?",
                        "? is the brother of ?",
                        "? and ? are the parents of ?",
                        "? is the uncle of ?",
                        "? is the father of ?",
                        "? is the grand father of ?",
                        "?, ? and ? are the children of ?",
                        "? is the son of ?",
                        "? is the aunt of ?"
        ]
        
        # a list of possible queestion patterns
        # same rules for statement patterns 
        # TODO: can you help me, double check if this is complete
        #       if it is, you can delete this thanks (zry)
        self.questions = [
                        "Are ? and ? siblings"
                        "Is ? a sister of ?"
                        "Is ? a brother of ?"
                        "Is ? the mother of ?"
                        "Is ? the father of ?"
                        "Are ? and ? the parents of ?"
                        "Is ? the grandmother of ?"
                        "Is ? a daughter of ?"
                        "Is ? a son of ?"
                        "Is ? a child of ?"
                        "Are ?, ? and ? children of ?"
                        "Is ? an uncle of ?"
                        "Who are the siblings of ?"
                        "Who are the sisters of ?"
                        "Who is the mother of ?"
                        "Who is the father of ?"
                        "Who are the parents of ?"
                        "Is ? a grandfather of ?"
                        "Who are the daughters of ?"
                        "Who are the sons of ?"
                        "Is ? an aunt of ?"
                        "Are ? and ? relatives"    
        ]

    def verify(self, string -> str) -> bool:
        """checks if the string is a possible statement or question
        
        Remark. this can be removed or disregarded if not useful,
                added for the sake of adding it.

        Remark. to use this, the string must be handled already,
                that is, the variables or constants in the statement or question
                are replaced with the ?        

        Args:
            string (str): the string 

        Returns:
            bool: (true) if string is in questions or statements, otherwise false
        """
        return True if string in self.questions or string in self.statements else False
    
    def remove_vars_and_consts(string) -> str:
        """Removed

        Args:
            string (_type_): _description_

        Returns:
            str: _description_
        """
        
