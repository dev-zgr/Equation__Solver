def rooter(numberto_root):


    """This function roots numbers and shows them in traditional representation like a√b"""

    operand = numberto_root
    prime_dictionary = dict()
    numberin = 1
    numberout = 1
    denominator = 2



    while operand != 1:
        if operand % denominator == 0:
            prime_dictionary[denominator] = 0
            while operand % denominator == 0:
                operand /= denominator
                prime_dictionary[denominator] += 1
            denominator+=1
        else:
            denominator += 1



    for key in prime_dictionary:

        if prime_dictionary[key] % 2 == 0:
            for i in range(int(prime_dictionary[key] / 2)):
                numberout *= key
        else:
            numberin *= key
            for i in range(int((prime_dictionary[key] - 1) / 2)):
                numberout *= key



    match (numberout ,numberin):
        case(x , 1):
            return f"{x}"
        case(1,x):
            return f"√{x}"
        case(x,y):
            return f"{x}√{y}"




def evaluater(list_abc):

    """This function calculates discrimiant of function than returns every individual ax² + bx + c  terms """
    a = list_abc[0]
    b = list_abc[1]
    c = list_abc[2]
    delta = b * b - 4 * a * c


    if delta > 0:
        return [delta , list_abc , rooter(delta)]
    elif delta == 0:
        return [delta , list_abc]
    else:
        return[delta , list_abc]
