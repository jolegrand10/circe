""" BMI module for handling body mass index calculations and related data."""


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate the Body Mass Index (BMI)
    given weight in kg and height in meters."""
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi: float) -> str:
    """Determine the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


if __name__ == "__main__":
    # Example usage
    weight = 70.0  # in kg
    height = 1.75  # in meters

    bmi_value = calculate_bmi(weight, height)
    category = bmi_category(bmi_value)
    print(f"BMI: {bmi_value}, Category: {category}")
    # Output: BMI: 22.86, Category: Normal weight
