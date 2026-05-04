import simple_calculator

def main():
    calculator = simple_calculator.Calculator()
    print("Not so Simple Calculator(Maangas)")

    while True:
        try:
            operation = input("Enter operation: ")
            if operation == "Square Root":
                number = input("Enter number: ")
                result = calculator.square_root(number)
            else:
                first_number = input("Enter first number: ")
                second_number = input("Enter second number: ")

                if operation == "Addition":
                    result = calculator.add(first_number, second_number)
                elif operation == "Subtraction":
                    result = calculator.subtract(first_number, second_number)
                elif operation == "Multiplication":
                    result = calculator.multiply(first_number, second_number)
                elif operation == "Division":
                    result = calculator.divide(first_number, second_number)
                elif operation == "Modulos":
                    result = calculator.modulus(first_number, second_number)
                elif operation == "Floor Division":
                    result = calculator.floor_division(first_number, second_number)

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()