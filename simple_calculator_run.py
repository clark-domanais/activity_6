import simple_calculator

def main():
    calculator = simple_calculator.Calculator()
    print("Not so Simple Calculator")

    while True:
        try:
            operation = input("Enter operation: ")

        except ValueError:
            print("Invalid input")