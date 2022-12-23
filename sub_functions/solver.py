def solver(info_list):
    a = info_list[1][0]
    b = info_list[1][1]
    c = info_list[1][2]
    if info_list[0] < 0:
        return[0]
    elif info_list[0] == 0:
        return[1 , -b / 2*a]
    else:
        if info_list[2].__contains__("√"):
            return[2 , f"({-b} - {info_list[2]}) /{2*a}" , f"({-b} + {info_list[2]}) / {2*a}"]
        else:
            return[2 , f"{(-b + int(info_list[2])) / 2 *a }" ,f"{(-b - int(info_list[2])) / 2 *a }"]

