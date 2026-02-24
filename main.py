# Objectives of main.py
# Accept a filename;
# Read it line by line;
# Pass lines to interpreter.

# Filename = .ss (stands for sim sim)
import os
from pathlib import Path
import interpreter

def get_dir() -> Path:
    current_dir = Path(__file__).resolve().parent
    return current_dir / "programs" / "math2.ss"

file_to_run = get_dir()

def file_exists():
    if not file_to_run.exists():
        print(f"File not found: {file_to_run}")
        exit(1)

def file_correct_suffix():
    if not file_to_run.suffix == ".ss":
        print(f"Not a .ss file: {file_to_run}")
        exit(1)

def read_lines() -> list:
    with open(file_to_run, "r") as file:
        list_of_lines = []
        for line in file:
            list_of_lines.append(line)
        return list_of_lines

interpreter = interpreter.Interpreter()


if __name__ == '__main__':
    print(f"Nice way: {file_to_run}")
    file_exists()
    file_correct_suffix()
    lines = read_lines()
    interpreter.interpret_lines(lines)

