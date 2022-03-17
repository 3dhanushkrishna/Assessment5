def isPalindrome(s):
    return s == s[::-1]
s = input("Enter the string: ")
ans = isPalindrome(s)

if ans:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")