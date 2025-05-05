import os
import re

def parse_tests(input_folder):
    """Parse plain English test inputs into structured test cases."""
    test_cases = {}
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            with open(os.path.join(input_folder, file_name), "r") as file:
                content = file.read()

            test_name = re.search(r"Test:\s*(.+)", content).group(1)
            steps = re.findall(r"\d+\.\s*(.+)", content)
            test_cases[test_name] = steps
    return test_cases