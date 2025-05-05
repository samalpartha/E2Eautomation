import os

def generate_test_scripts(test_name, steps):
    """Generate Python test scripts from structured steps."""
    file_name = f"generated_tests/test_{test_name.replace(' ', '_').lower()}.py"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w") as file:
        file.write(f"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_{test_name.replace(' ', '_').lower()}():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        """)
        for step in steps:
            if "navigate to" in step.lower():
                url = step.split(" to ")[-1].strip('"')
                file.write(f'        driver.get("{url}")\n')
            elif "enter" in step.lower():
                field = re.search(r'in the (.+?) field', step).group(1)
                value = re.search(r'enter "(.+?)"', step).group(1)
                file.write(f'        driver.find_element(By.NAME, "{field}").send_keys("{value}")\n')
            elif "click" in step.lower():
                button = re.search(r'click the (.+?) button', step).group(1)
                file.write(f'        driver.find_element(By.ID, "{button}").click()\n')
            elif "verify" in step.lower():
                condition = re.search(r'verify that (.+)', step).group(1)
                file.write(f'        assert "{condition}" in driver.page_source\n')
        file.write("""
    finally:
        driver.quit()
""")