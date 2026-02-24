import operator
class Interpreter:
    def __init__(self):
        self.variables = {}

    def line_classification(self, line) -> str:
        new_line = line.strip()

        if len(new_line) == 0:
            return "empty"

        if new_line.startswith("$"):
            return "comment"

        if new_line.startswith('print ->'):
            return "print"

        if "=" in new_line:
            return "assignment"

        return "error"

    def evaluate_value(self, value) -> int:
        if value.startswith("@"):
            new_value = value[1:]
            return new_value

        elif value.isnumeric():
            new_value = int(value)
            return new_value

        elif not value.isnumeric() and value in self.variables:
            return self.variables[value]

        elif "+" in value:
            expression_left = value.partition("+")[0].strip()
            expression_right = value.partition("+")[2].strip()
            left_value = self.evaluate_value(expression_left)
            right_value = self.evaluate_value(expression_right)
            sum_value = left_value + right_value
            return sum_value

        elif "-" in value:
            expression_left = value.partition("-")[0].strip()
            expression_right = value.partition("-")[2].strip()
            left_value = self.evaluate_value(expression_left)
            right_value = self.evaluate_value(expression_right)
            sum_value = left_value - right_value
            return sum_value

        raise Exception("No value to store")

    def assignment(self, line):
        name = line.partition("=")[0].strip()
        value = line.partition("=")[2].strip()
        new_value = self.evaluate_value(value)
        self.variables[name] = new_value

    def printing(self, line):
        value = line.partition("print ->")[2].strip()
        new_value = self.evaluate_value(value)
        print(new_value)

    def line_handler(self, line_type, line, line_number):
        if line_type == "assignment":
            self.assignment(line)

        if line_type == "print":
            self.printing(line)

        if line_type == "error":
            raise Exception(f"Unknown instruction in line {line_number}: {line}")

    def interpret_lines(self, list_of_lines):
        line_number = 1
        for line in list_of_lines:
            line_type = self.line_classification(line)
            self.line_handler(line_type, line, line_number)
            line_number += 1


