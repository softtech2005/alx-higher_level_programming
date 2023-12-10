def print_last_digit(number):
    # Get the last digit using the remainder when dividing by 10
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

# Testing the function
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
