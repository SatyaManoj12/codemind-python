def is_self_dividing(number):
    num_str = str(number)
    for digit in num_str:
        if digit == '0' or number % int(digit) != 0:
            return False
    return True

def find_self_dividing_numbers(start, end):
    self_dividing_numbers = []
    for num in range(start, end + 1):
        if is_self_dividing(num):
            self_dividing_numbers.append(num)
    return self_dividing_numbers

# Example usage
start_num = int(input())
end_num = int(input())

self_dividing_nums = find_self_dividing_numbers(start_num, end_num)
self_dividing_nums= ' '.join(map(str,self_dividing_nums ))
print(self_dividing_nums)
