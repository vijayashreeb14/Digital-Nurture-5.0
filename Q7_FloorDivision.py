def split_bill(total_bill, people):
    if people <= 0:
        print("Invalid Number of People")
        return

    share = total_bill // people
    print(f"Each Person Pays: {share}")

total_bill = 1250
people = 4

split_bill(total_bill, people)