from art import logo
from os import system

print(logo)

operation_signs = ["+", "-", "*", "/"]


def print_operation_signs():
    """Print out one of defined operation signs"""
    for sign in operation_signs:
        print(sign)


def get_calculated_result(number1, number2, operation_sign):
    """Return calculated result according to provided numbers and operation sign.
    In case of inappropriate number or sign function returns None"""
    if type(number1) != float or type(number2) != float:
        print("Provide correct numbers")
        return None

    if operation_sign.strip() == operation_signs[0]:
        return number1 + number1
    elif operation_sign.strip() == operation_signs[1]:
        return number1 - number2
    elif operation_sign.strip() == operation_signs[2]:
        return number1 * number2
    elif operation_sign.strip() == operation_signs[3]:
        return number1 / number2
    else:
        print("You provide wrong operation")
        return None


def get_and_print_result_statement(number1, number2, operation_sign):
    """Return and print out calculated result according to provided numbers and operation sign.
    In case of inappropriate number or sign function returns None and print out nothing"""
    result = get_calculated_result(number1, number2, operation_sign)
    if result:
        print(f"{number1} {operation_sign} {number2} = {result}")
        return result
    else:
        return None


def restart_calculation():
    """Function restarting calculation process"""
    print("Your calculation will be restarted")
    system("clear")
    print(logo)
    run_calculator()


def run_calculator():
    """Main function for runnig calculator program"""
    continue_calculation_flag = "y"

    try:
        first_number = float(input("What's the first number? "))
        print_operation_signs()

        while True:

            operation_sign = input("Pick an operation: ")
            second_number = float(input("What's the next number? "))

            result = get_and_print_result_statement(
                first_number, second_number, operation_sign)

            if not result:
                restart_calculation()

            continue_calculation_flag = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation (any other typed value will close the program): ")
            should_calculation_continue = True if continue_calculation_flag == "y" else False
            first_number = result

            if not should_calculation_continue:
                break
    except:
        restart_calculation()

    if continue_calculation_flag == "n":
        restart_calculation()


run_calculator()
