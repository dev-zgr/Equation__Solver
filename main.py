from sub_functions import *
def equation_solver(equation):
    if checker.checker(equation)[0] == True:
        result_checker = checker.checker(equation)[1]
        result_extroctor = extroctor.extractor(result_checker)
        result_evaluater = evaluater.evaluater(result_extroctor)
        result_solver = solver.solver(result_evaluater)
        match result_solver[0]:
            case 0:
                print("This equation has no solution")
            case 1:
                print(f"This equation has only solution. \n solve set = ({result_solver[1]})")
            case 2:
                print(f"This equation has two solution \n solve set = ({result_solver[1]} , {result_solver[2]})")
    else:
        if checker.checker(equation)[1] == 0:
            print("dont use invalid letters . only x is allowed and avoid other symbols!")
        else:
            print("dont use more than 2 characters between term!")

equation = input("Enter equation to see solve set , type \"end\" to quit.\n")
while equation != "end":
    equation_solver(equation)
    equation = input("Enter equation to see solve set , type \"end\" to quit.\n")

