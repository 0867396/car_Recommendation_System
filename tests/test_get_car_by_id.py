import pytest
import os
import sys

# Add the absolute path to the parent directory of car_Recommendation_System
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from car_Recommendation_System.get_car_data import get_car_by_id

# Test cases
test_cases = [
    (1, [(1, 'Honda', 'Amaze 1.2 VX i-VTEC', 505000, 2017, 87150, 'Petrol', 'Manual', 'Pune', 'Grey', 'First', 'Corporate', '1198 cc', 3990, 1680, 1505, 5, 35)]),
    (3, [(3, 'Hyundai', 'i10 Magna 1.2 Kappa2', 220000, 2011, 67000, 'Petrol', 'Manual', 'Lucknow', 'Maroon', 'First', 'Individual', '1197 cc', 3585, 1595, 1550, 5, 35)]),
]

# Test function
@pytest.mark.parametrize("vehicle_id, expected_result", test_cases)
def test_get_car_by_id(vehicle_id, expected_result):
    # Call the function to get the result
    result = get_car_by_id(vehicle_id)

    # Assert the result
    assert result == expected_result