def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

# Example usage
start_num =int(input())
end_num =int(input())

prime_count = count_primes(start_num, end_num)
print(prime_count)
