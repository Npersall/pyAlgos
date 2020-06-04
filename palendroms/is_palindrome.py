
def is_palindrome(string):
    string = "".join(p for p in string if p not in ('!','.',':','?',' '))
    string = string.lower()
    print(string)
    return string == string[::-1]


