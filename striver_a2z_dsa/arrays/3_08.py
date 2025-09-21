# Union of Two Sorted Arrays

def findUnion(first_list, second_list):
    i, j = 0, 0
    union_list = []

    while i < len(first_list) and j < len(second_list):
        if first_list[i] <= second_list[j]:
            if len(union_list) == 0 or union_list[-1] != first_list[i]:
                union_list.append(first_list[i])
            i += 1
        else:
            if len(union_list) == 0 or union_list[-1] != second_list[j]:
                union_list.append(second_list[j])
            j += 1

    while i < len(first_list):
        if union_list[-1] != first_list[i]:
            union_list.append(first_list[i])
        i += 1

    while j < len(second_list):
        if union_list[-1] != second_list[j]:
            union_list.append(second_list[j])
        j += 1

    return union_list


if __name__ == "__main__":
    first_list_value = [1, 1, 24, 24, 32, 32, 100]
    second_list_values = [1, 2, 3, 4, 4, 5]

    print(findUnion(first_list_value, second_list_values))
