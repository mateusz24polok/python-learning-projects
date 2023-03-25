from art import logo

print(logo)

operation_signs = ["+", "-", "*", "/"]

def print_operation_signs():
    for sign in operation_signs:
        print(sign)

def get_calculated_result(number1, number2, operation_sign):
    if type(number1) != float or type(number2) != float:
        print("Provide correct numbers")
        return None

    if operation_sign == operation_signs[0]:
        return number1 + number1
    elif operation_sign == operation_signs[1]:
        return number1 - number2
    elif operation_sign == operation_signs[2]:
        return number1 * number2
    elif operation_sign == operation_signs[3]:
        return number1 / number2
    else:
        print("You provide wrong operation")
        return None
    
def print_result_statement(number1, number2, operation_sign):
    result = get_calculated_result(number1, number2, operation_sign)
    if result:
        print(f"{number1} {operation_sign} {number2} = {result}")
    
first_number = float(input("What's the first number? "))
print_operation_signs()
operation_sign = input("Pick an operation: ")
second_number = float(input("What's the next number? "))

print_result_statement(first_number, second_number, operation_sign)
