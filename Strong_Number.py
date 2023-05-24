number = int(input())
temp = number
sum_factorials = 0

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_factorials += factorial
    temp //= 10

is_strong = sum_factorials == number

if is_strong:
    print("The number",number,"is a strong number")
else:
    print("The number",number,"is not a strong number")
