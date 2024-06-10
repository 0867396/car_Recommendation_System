import pytest
import os
import sys

# Add the absolute path to the parent directory of car_Recommendation_System
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from car_Recommendation_System.prediction import get_label_prediction


# Test function
@pytest.mark.parametrize("description, expected_label", [
    ("ik wil een kleine auto", "kleine wagens"),
    ("Sportwagen met handmatige transmissie en sportophanging voor ultieme controle.", "geschikt voor liefhebbers van autorijden"),
])
def test_get_label_id_by_name(label_name, expected_result):
    # Call the function to get the result
    result = get_label_prediction(label_name)

    # Assert the result
    if expected_result is None:
        assert result == []  # Expecting empty list for non-existent label
    else:
        assert result == label_name
