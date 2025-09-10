# Find the highest/lowest frequency element

if __name__ == "__main__":
    listElements = [1, 3, 4, 1, 44, 3, 1, 3, 4, 1, 4, 4, 4]
    freq = {}

    for ele in listElements:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    max_freq = max(freq.values())

    most_freq_ele = [key for key, value in freq.items() if value == max_freq]

    print(f"Max freq element: {max_freq}")
    print(f"Most freq element: {most_freq_ele}")
