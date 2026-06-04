def first_even(limit):
    if limit <= 0:
        print("Invalid Range")
        return

    for i in range(limit):
        if i % 2 == 0:
            print("First Even Number:", i)
            break

first_even(10)