import os
import subprocess

def run_tests():
    """Run all tests and generate Allure reports."""
    test_dir = "generated_tests"
    os.makedirs(test_dir, exist_ok=True)
    subprocess.run(["pytest", test_dir, "--alluredir=reports/"])
    subprocess.run(["allure", "serve", "reports/"])