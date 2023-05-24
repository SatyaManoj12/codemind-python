def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(str(num)):
            palindromes.append(num)
    return palindromes

# Example usage
start_num = int(input())
end_num = int(input())

palindrome_numbers = find_palindromes(start_num, end_num)
palindrome_string = ' '.join(map(str, palindrome_numbers))
print(palindrome_string)

