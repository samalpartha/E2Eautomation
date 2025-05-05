from utils.test_runner import run_tests
from ai.nlp_parser import parse_tests
from utils.code_generator import generate_test_scripts

def main():
    # Step 1: Parse plain-English test inputs
    print("Parsing test inputs...")
    parsed_tests = parse_tests("test_inputs/")

    # Step 2: Generate test scripts
    print("Generating test scripts...")
    for test_name, test_details in parsed_tests.items():
        generate_test_scripts(test_name, test_details)

    # Step 3: Run the tests
    print("Running tests...")
    run_tests()

if __name__ == "__main__":
    main()