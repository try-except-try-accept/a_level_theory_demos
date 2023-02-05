
INVALID = "invalid expression"
RED = "\n\033[38;2;254;0;0m"
GREEN = "\n\033[38;2;0;254;0m"
WHITE = "\033[38;2;254;254;254m"

def get_terms(exp):
    '''Retrieve boolean terms from expression'''
    return sorted(list(set(char for char in exp if char.isalpha())))

###################################################

def eval_exp(exp, bits, terms):
    '''Pythonise boolean expression and then evaluate with given input bits'''
    exp = exp.replace("!", " not ")
    exp = exp.replace("+", " or ")
    exp = exp.replace(".", " and ")
    exp = exp.replace("AND", " and ")
    exp = exp.replace("OR", " or ")
    exp = exp.replace("NOT", " not ")

    bits = list(bits)

    if terms:
        while bits:
            exp = exp.replace(terms.pop(0), bits.pop(0))

    exp = "".join("0" if char.isupper() else char for char in exp)    
    exp = exp.replace("1", "True").replace("0", "False")
        
    try:     
        return str(int(eval(exp))), ""
    except Exception as e:       
        return INVALID, exp+e

###################################################

def compute_truth_table(exp, terms):
    '''Compute / display truth table for expression and return results'''
    headings = ""    

    for term in terms:
        headings += term.center(3) + "|"

    exp_length = len(exp)    
    headings += " " + exp
    print(headings)
    n_terms = len(terms)
    results = []
        
    for i in range(2 ** n_terms):
        print(" ", end="")
        bits = bin(i)[2:].zfill(n_terms)
        res, error = eval_exp(exp, bits, list(terms))
        results.append(res)
        print(" | ".join(str(b) for b in bits) + f" | {results[-1]}")

        if res == INVALID:
            break

    print(RED+error)
    print(WHITE+" ")

    return results

###################################################

def get_exp(n):
    '''Get expression from user'''
    exp = input(f"Enter {n} expression:  ")

    ## TODO later - syntax validation
    return exp

###################################################

def check_simp():
    '''Compare two simplifications and inform user if match found'''
    
    print(f"""{WHITE}When entering expressions
use UPPERCASE for terms only.
You may use either GCSE-style logic notation OR boolean algebra notation.
(use ! for NOT instead of an overline)

Examples:
------------
!(!A.!B)+(C.!D)

not(not a and not b) or (c and not d)
""")

    exp1 = get_exp("the original")
    exp2 = get_exp("your simplified")

    terms = get_terms(exp1)

    print()
    print("Evaluating", exp1)
    print()
    res1 = compute_truth_table(exp1, terms)
    print()
    print("Evaluating", exp2)
    print()
    res2 = compute_truth_table(exp2, terms)

    if res1 != res2:
        print(RED+"X Your boolean simplification did not work - results do not match.\n")
    else:
        print(GREEN+"✓ Your boolean simplification worked - results matched. 🎉")
        print()

###################################################

if __name__ == "__main__":
    while True:
        check_simp()
        



    

        

        

    

    
