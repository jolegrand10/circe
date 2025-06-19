from bmi.bmi import calculate_bmi, bmi_category


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == '__main__':
    main()