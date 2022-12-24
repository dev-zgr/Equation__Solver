
from sub_functions import *
# import chechker , evaluater , extractor , solver from sub_fucntions package

def equation_solver(equation):

    """This functions includes the composition and working system of these functions."""

    if checker.checker(equation)[0] == True:


        # while equation in true format
        result_checker = checker.checker(equation)[1]                       # assign variable to parsed coefficents
        result_extroctor = extroctor.extractor(result_checker)              # extact coefficents
        result_evaluater = evaluater.evaluater(result_extroctor)            # evaluate them respect to discriminat
        result_solver = solver.solver(result_evaluater)                     # solve equation


        match result_solver[0]:                                             # print output for appoite solutions
            case 0:
                print("This equation has no solution")
            case 1:
                print(f"This equation has only solution. \n solve set = ({result_solver[1]})")
            case 2:
                print(f"This equation has two solution \n solve set = ({result_solver[1]} , {result_solver[2]})")
    else:
        if checker.checker(equation)[1] == 0:                      # if equation isnt forms to valid form warn the user
            print("dont use invalid letters . only x is allowed and avoid other symbols!")
        else:
            print("dont use more than 2 characters between term!")





equation = input("Enter equation to see solve set , type \"end\" to quit.\n")   #initial command


while equation != "end":                                                        #while you dont type end function works
    equation_solver(equation)
    equation = input("Enter equation to see solve set , type \"end\" to quit.\n")

