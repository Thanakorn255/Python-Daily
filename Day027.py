def palindrome(s:str):
    if s == s[::-1]:
        return True
    return False
inp = input()
print(palindrome(inp))