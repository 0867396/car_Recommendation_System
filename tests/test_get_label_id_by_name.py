import pytest
import os
import sys

# Add the absolute path to the parent directory of car_Recommendation_System
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from car_Recommendation_System.get_car_data import get_label_id_by_name

# Define test cases
test_cases = [
    ("geschikt voor gezinnen", 1),
    ("geschikt voor woon-werkverkeer", 2),
    ("geschikt voor liefhebbers van autorijden", 3),
    ("non-existent label", None)  # Test case for non-existent label
]

# Test function
@pytest.mark.parametrize("label_name, expected_result", test_cases)
def test_get_label_id_by_name(label_name, expected_result):
    # Call the function to get the result
    result = get_label_id_by_name(label_name)

    # Assert the result
    if expected_result is None:
        assert result == []  # Expecting empty list for non-existent label
    else:
        assert result == [(expected_result, label_name)]  # Expecting tuple with label ID and name
