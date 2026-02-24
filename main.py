# Objectives of main.py
# Accept a filename;
# Read it line by line;
# Pass lines to interpreter.

# Filename = .ss (stands for sim sim)
import sys
from pathlib import Path
import interpreter

def cli_handling() -> Path:
    if len(sys.argv) > 1:
        path = Path(__file__).parent / sys.argv[1]
        return path
    else: print("No arguments provided")
    exit(1)

def file_exists(file_to_run):
    if not file_to_run.exists():
        print(f"File not found: {file_to_run}")
        exit(1)

def file_correct_suffix(file_to_run):
    if not file_to_run.suffix == ".ss":
        print(f"Not a .ss file: {file_to_run}")
        exit(1)

def read_lines(file_to_run) -> list:
    with open(file_to_run, "r") as file:
        list_of_lines = []
        for line in file:
            list_of_lines.append(line)
        return list_of_lines

interpreter = interpreter.Interpreter()


if __name__ == '__main__':
    file_to_run = cli_handling()
    file_exists(file_to_run)
    file_correct_suffix(file_to_run)
    lines = read_lines(file_to_run)
    interpreter.interpret_lines(lines)

