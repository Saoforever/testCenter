
# Ask the user for a number with input()
# Try converting it to int and print it doubled
# If they type something that's not a number, catch it and print a friendly message

while True:
    try:
        num = int(input("Enter a number here: "))
        print(num*2)
        break
    except:
        print("Error: Invalid Response, input number ")
