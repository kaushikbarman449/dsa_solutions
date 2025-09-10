# Hashing character count taking all ASCII space 255

if __name__ == "__main__":
    charCheck = input()
    InputString = "Encyclopedia"

    hashList = [0] * 255
    for i in range(len(InputString)):
        hashList[ord(InputString[i])] += 1

    print(hashList[ord(charCheck)])
