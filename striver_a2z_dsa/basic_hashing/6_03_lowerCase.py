# Hashing character count taking lower case characters

if __name__ == "__main__":
    charCheck = input("Enter lower case character: ").lower()
    inputString = input("Enter your string: ").lower()

    hashList = [0] * 26

    for ch in inputString:
        hashList[ord(ch) - ord('a')] += 1

    print(hashList[ord(charCheck) - ord('a')])
