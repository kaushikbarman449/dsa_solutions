# Hashing character count using python dictionary

if __name__ == "__main__":
    charCheck = input()
    InputString = "Encyclopedia"
    freq = {}

    for ch in InputString:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print(freq[charCheck])
