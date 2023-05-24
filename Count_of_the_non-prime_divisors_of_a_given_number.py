def count_non_prime_divisors(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            if is_prime(i) == False:
                count += 1
    return count
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
 
N = int(input())
print(count_non_prime_divisors(N))