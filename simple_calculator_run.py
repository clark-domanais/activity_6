import simple_calculator

if __name__ == "__main__":
    calculator = simple_calculator.Calculator()
    print("Not so Simple Calculator(Maangas)")

    while True:
        try:
            operation = input("Enter operation (Addition, Subtraction, Multiplication, Division, Modulo, Floor Division, Square Root): ")
            if operation == "Square Root":
                number = int(input("Enter number: "))
                result = calculator.square_root(number)
            else:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))

                if operation == "Addition":
                    result = calculator.add(first_number, second_number)
                elif operation == "Subtraction":
                    result = calculator.subtract(first_number, second_number)
                elif operation == "Multiplication":
                    result = calculator.multiply(first_number, second_number)
                elif operation == "Division":
                    result = calculator.divide(first_number, second_number)
                elif operation == "Modulo":
                    result = calculator.modulo(first_number, second_number)
                elif operation == "Floor Division":
                    result = calculator.floor_division(first_number, second_number)

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input")
        if input("Continue? (Y/N): ").lower() != "y":
            break