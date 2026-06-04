def kg_to_pounds():
    kg = float(input("Enter weight in kg: "))

    if kg < 0:
        print("Invalid Weight")
        return

    pounds = kg * 2.20462
    print(f"Weight in Pounds: {pounds:.2f}")

kg_to_pounds()