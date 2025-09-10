# Counting frequencies of array elements

if __name__ == "__main__":
    listElements = [1, 3, 4, 1, 44, 3, 1, 3, 4, 1]
    freq = {}

    for ele in listElements:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    for key, value in freq.items():
        print(f"Element {key} appears {value} times")
