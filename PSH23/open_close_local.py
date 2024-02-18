
string = "{{}}{}[[][]]()([()]{})([]){}{}{(([]))}[](())[]{}[[{}][[[[]()]]()]{}](]{()[][]}[[[]]]({{()()}{}()([[][]{}](())){()}}(()[[])))"

def verify_v2(string):
    count_brace = 0
    count_bracket = 0
    count_par = 0

    for char in string:      
        if char == '{':
            print("+1")
            count_brace += 1
        elif char == '}':
            print("-1")
            count_brace -= 1
        elif char == '[':
            print("+1")
            count_bracket += 1
        elif char == ']':
            print("-1")
            count_bracket -= 1
        elif char == '(':
            print("+1")
            count_par += 1
        elif char == ')':
            print("-1")
            count_par -= 1
        if count_brace < 0 or count_par < 0 or count_bracket < 0:    
            break  

    if count_brace == 0 and count_par == 0 and count_bracket == 0:
        print("True")
    else:
        print("False")

verify_v2(string)

#TODO : Ajouter si les termes sont bien dans l'ordre ect... comme dans l'énoncé.