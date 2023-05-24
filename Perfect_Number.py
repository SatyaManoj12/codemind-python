def is_perfect_number(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number
number = int(input())
is_perfect = is_perfect_number(number)
if is_perfect:
    print("True")
else:
    print("False")
