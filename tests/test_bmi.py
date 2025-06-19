from bmi.bmi import calculate_bmi, bmi_category

EPSILON = 0.01


def test_calculate_bmi():
    assert abs(calculate_bmi(70, 1.75) - 22.86) <= EPSILON
    assert abs(calculate_bmi(60, 1.60) - 23.44) <= EPSILON
    assert abs(calculate_bmi(80, 1.80) - 24.69) <= EPSILON
    assert abs(calculate_bmi(90, 1.85) - 26.29) <= EPSILON


def test_bmi_category():
    assert bmi_category(22.86) == "Normal weight"
    assert bmi_category(23.44) == "Normal weight"
    assert bmi_category(24.69) == "Normal weight"
    assert bmi_category(26.29) == "Overweight"
    assert bmi_category(18.5) == "Normal weight"
    assert bmi_category(30) == "Obesity"
    assert bmi_category(35) == "Obesity"
    assert bmi_category(40) == "Obesity"
