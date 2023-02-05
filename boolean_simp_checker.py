
INVALID = "invalid expression"

def get_terms(exp):

    return sorted(list(set(char for char in exp if char.isalpha())))


def eval_exp(exp, bits, terms):

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
     
        return str(int(eval(exp)))
    except Exception as e:
        print(exp)
        print(e)
        return INVALID



def compute_truth_table(exp, terms):

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
        results.append(eval_exp(exp, bits, list(terms)))
        print(" | ".join(str(b) for b in bits) + f" | {results[-1]}")

        if results[-1] == INVALID:
            break

    return results


def get_exp(n):
    exp = input(f"Enter {n} expression:  ")

    ## TODO later - syntax validation
    return exp


def check_simp():

    print("""\033[38;2;254;254;254mWhen entering expressions
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
        print("\n\033[38;2;254;0;0m"+"X Your boolean simplification did not work - results do not match.\n")
    else:
        print("\n\033[38;2;0;254;0m"+"✓ Your boolean simplification worked - results matched. 🎉")
        print()


if __name__ == "__main__":
    while True:
        check_simp()
        



    

        

        

    

    
