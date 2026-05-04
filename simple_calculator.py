import math

class Calculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number
    def multiply(self, first_number, second_number):
        return first_number * second_number
    def divide(self, first_number, second_number):
        return first_number / second_number
    def power(self, first_number, second_number):
        return first_number ** second_number
    def modulos(self, first_number, second_number):
        return first_number % second_number
    def floor_division(self, first_number, second_number):
        return first_number // second_number
    def square_root(self, first_number):
        if first_number >= 0:
            return math.sqrt(first_number)
        return "Error: Negative numbers are not allowed"