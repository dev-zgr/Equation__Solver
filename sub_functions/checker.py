forbidden_character = {"Q", "q" ,"W", "w" ,"e" ,"E" ,"R" ,"r" , "t", "T" , "y" ,"Y" ,"U" ,"u" ,"I" "i" ,"O" ,"o" , "P" ,"p" ,"a" ,"A" ,"D" ,"d" ,"f" ,"F" ,"G" , "g" ,"H" ,"h" ,"J", "j" ,"k" , "K" ,"L" ,"l" , "Z" ,"z" ,"c" ,"v" ,"b", "n" ,"m" , "C", "V",  "B" , "N" "M" , "!" ,"'", '"' ,"^" ,"%" ,"&", "/", "(" ,")" ,"?"}
forbidden_character.union({"P" ,"p" ,"a" ,"A" ,"D" ,"d" ,"f" ,"F" ,"G" , "g" ,"H" ,"h" ,"J", "j" ,"k" , "K" ,"L" ,"l"})
def checker(equation):
    set_equation = set(equation)
    term_range = []
    meaninful_range = []
    if set_equation.intersection(forbidden_character) != set():
        return [False, 0]
    for index in range(len(equation)):
        if equation[index] == "+" or equation[index] == "-":
            term_range.append(index)

    if term_range[0] != 0:
        term_range.insert(0, 0)
    if term_range[len(term_range) -1] != len(equation) -1:
        term_range.append(len(equation))

    for item in range(len(term_range)-1) :
        meaninful_range.append(equation[term_range[item]: term_range[item + 1]])
    if meaninful_range[0].__contains__("+") == False and meaninful_range[0].__contains__("-") == False:
        meaninful_range[0] = "+" + meaninful_range[0]
    for items in meaninful_range:
        sentinel = 0
        for character in range(len(items)):
            if items[character] != " " and items[character] != "+" and items[character] != "-":
                if (character - sentinel > 3  and sentinel != 0 ):
                    return [False , 1]
                sentinel = character + 1


    return [True,  meaninful_range]



