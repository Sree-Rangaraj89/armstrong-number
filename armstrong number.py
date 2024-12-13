def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = 0
    
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    if sum_of_powers == number:
        return True
    else:
        return False

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
