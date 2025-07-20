import pytest
import csv
from airport.checkin import Suitcase, Gate

GATE1 = Gate(53, 12000)
GATE2 = Gate(1827, 1738)


def test_gate_output(mocker):
    # TODO:
    # Use mocker.patch.object to override the check_price method of the Gate class.
    # If any dimension of the suitcase is greater than 500, it should return "543.21".
    # Otherwise, it should return "124.45".
    pass




# TODO:
# 1. Create a Suitcase object that can pass through the global GATE1 (can_pass_gate returns True).
# 2. Write another test case where a Suitcase cannot pass through GATE1 (can_pass_gate returns False).
# 3. Use the result_collector fixture to record both results and ensure they are saved to the output CSV file.
def test_gate1():
    pass


# TODO:
# 1. Create a Suitcase object that can pass through the global GATE2 (can_pass_gate returns True).
# 2. Write another test case where a Suitcase cannot pass through GATE2 (can_pass_gate returns False).
# 3. Use the result_collector fixture to record both results and ensure they are saved to the output CSV file.
def test_gate2():
    pass

