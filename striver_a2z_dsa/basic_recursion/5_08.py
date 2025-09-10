# Check if a string is palindrome or not

def check_palindrome(start, wordString):
    N = len(wordString) - 1

    if start >= N / 2:
        return True

    if wordString[start] != wordString[N - start]:
        return False
    else:
        return check_palindrome(start + 1, wordString)


if __name__ == "__main__":
    wordString = "112211"
    result = check_palindrome(0, wordString)
    print(result)
