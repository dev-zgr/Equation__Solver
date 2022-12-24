numbers = {"0", "1" ,"2" ,"3" ,"4" ,"5" , "6" ,"7" ,"8" ,"9"}
empty_set = set()
def extractor(meaningful_values):
    """This function determines the coefficent of value terms like  a , b and c in ax²+bx + c"""

    abc = [0, 0, 0]
    for items in range(len(meaningful_values)):

        raw_string = ""


        for characters in meaningful_values[items]:
            if characters != " ":
                raw_string += characters

        if set(raw_string).intersection(numbers) == empty_set:
            raw_string = raw_string[0] + "1" + raw_string[1:]
        meaningful_values[items] = raw_string



    for items in meaningful_values:
        if items.__contains__("²"):
            abc[0] += int(items[0: len(items) -2])
        elif items.__contains__("x"):
            abc[1] += int(items[0: len(items) -1])
        else:
            abc[2] += int(items)
    return abc
