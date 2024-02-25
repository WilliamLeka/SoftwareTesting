class Calculator:
    def __init__(self, input_str):
        self.input_str = input_str
        self.result = 0

    def calculate(self):
        # Split the input string into numbers and operation
        input_list = self.input_str.split(',')

        # Check if the number of elements is valid
        if len(input_list) < 3:
            raise ValueError("Invalid number of elements in input")

        elif len(input_list) > 5:
            numbers = list(map(float, input_list[:4]))

        else:
            # Extract numbers and operation
            numbers = list(map(float, input_list[:-1]))

        operation = input_list[-1]

        # Perform the calculation based on the operation
        if operation == '+':
            for num in numbers:
                self.result = self.result + num
        elif operation == '-':
            self.result = numbers[0] - numbers[1]
        elif operation == '*':
            self.result = 1
            for num in numbers:
                self.result *= num
        elif operation == '/':
            if numbers[1] == 0:
                if numbers[0] >= 0:
                    self.result = float('inf')
                else:
                    self.result = float('-inf')
            else:
                self.result = numbers[0] / numbers[1]
        else:
            raise ValueError("Invalid operation")

        return self.result

# Example usage:
calculator_instance = Calculator("1,2,3,4,+")
result = calculator_instance.calculate()
print(result)
