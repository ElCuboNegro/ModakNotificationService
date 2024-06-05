import os
import subprocess
import re
from behave import given, when, then
from commons import get_project_root, read_moo_count



@given('I have installed modak-notificationservice')
def modak_installed(context):
    # Check if modak is installed
    result = subprocess.run(["modak", "--version"], capture_output=True, text=True)
    # I have a variable to store the initial mooed times
    context.initial_mooed_times = read_moo_count()
    assert result.returncode == 0, "modak-notificationservice is not installed"


@when('I execute the modak command "moo"')
def step_impl(context):
    # Execute the command and store the result
    result = subprocess.run(["modak", "moo"], capture_output=True, text=True)
    # Extract the number of times mooed from the result
    context.result = result
    match = re.search(r'You have mooed (\d+) times', result.stdout)
    if match:
        context.mooed_times = int(match.group(1))
    else:
        context.mooed_times = 0

@then('I should get a successful exit code')
def step_impl(context):
    # Check if the exit code is 0
    assert context.result.returncode == 0, f"Command failed with exit code {context.result.returncode}"

@then('I should get a increment in the variable stored in the user_directory/.moo directory')
def step_impl(context):
    # Verify the increment
    assert context.mooed_times == context.initial_mooed_times + 1, f"The variable did not increment correctly, initial: {context.initial_mooed_times}, current: {context.mooed_times}"
