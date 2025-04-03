def is_even_and_divisible_by_3(n):
    return n % 2 == 0 and n % 3 == 0
num = int(input("Enter a number: "))
if is_even_and_divisible_by_3(num):
    print("True - The number is even and divisible by 3.")
else:
    print("False - The number is not even and divisible by 3.")
