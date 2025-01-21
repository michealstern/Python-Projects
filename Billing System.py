while True:
    name = input("Enter customer's name: ")
    total = 0

    while True:
        print("***** Enter the amount and quantity *****")
        amount = float(input("\nEnter amount: "))
        quantity = float(input("Enter quantity: "))

        total += amount*quantity
        repeat = input("\nDo you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No" or repeat == "NO":
            break

    print("-"*40)
    print(f"Name: {name}")
    print(f"Amount to be paid: {total}")
    print("-"*40)
    print("********* Happy Shopping *********\n")

    repeat1 = input("Do you want go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat == "No" or repeat == "NO":
        break