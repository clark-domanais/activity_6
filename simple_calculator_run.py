import simple_calculator

if __name__ == "__main__":
    calculator = simple_calculator.Calculator()
    print("Not so Simple Calculator(Maangas)")

    while True:
        try:
            operation = input("Enter operation (+, -, *, /, %, //, sqrt)): ")
            if operation == "sqrt":
                number = int(input("Enter number: "))
                result = calculator.square_root(number)
            else:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))

                if operation == "+":
                    result = calculator.add(first_number, second_number)
                elif operation == "-":
                    result = calculator.subtract(first_number, second_number)
                elif operation == "*":
                    result = calculator.multiply(first_number, second_number)
                elif operation == "/":
                    result = calculator.divide(first_number, second_number)
                elif operation == "%":
                    result = calculator.modulo(first_number, second_number)
                elif operation == "//":
                    result = calculator.floor_division(first_number, second_number)
                else:
                    raise ValueError("Invalid operation")

            print(f"Result: {result}")

        except ValueError as e:
            print(e)
        if input("Continue? (Y/N): ").lower() != "y":
            break