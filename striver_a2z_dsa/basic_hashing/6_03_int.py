# Hashing integer count using python dictionary

if __name__ == "__main__":
    charCheck = int(input())
    InputString = [1, 2, 1, 3]
    freq = {}

    for ch in InputString:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    if charCheck in freq:
        print(freq[charCheck])
    else:
        print(0)
