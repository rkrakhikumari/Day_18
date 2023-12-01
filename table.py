def print_table(number):
    print(f"Table of {number}")
    for i in range(1,11):
        result = number * i
        print(f"{number} * {i} = {result}")


while True:
    try:
        user_input = int(input("Enter a number between 1 and 10: "))
        if 1 <= user_input <=10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. please enter a valid number.")

print_table(user_input)
