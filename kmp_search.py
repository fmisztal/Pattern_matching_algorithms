def prefix_table(string):
    table = [0] * len(string)
    i = 0
    j = 1
    while j < len(string):
        if string[i] == string[j]:
            table[j] = i + 1
            i += 1
            j += 1
        elif i > 0:
            i = table[i - 1]
        else:
            table[j] = 0
            j += 1
    return table

def find_kmp(string, text):
    results = []
    if not string:
        return results
    table = prefix_table(string)
    i = 0
    j = 0
    while i < len(text):
        if string[j] == text[i]:
            i += 1
            j += 1
            if j == len(string):
                results.append(i - j)
                j = table[j - 1]
        else:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1
    return results


if __name__ == '__main__':
    print(find_kmp("acacagt", "asfacacagtasdacacacacagtagtacacagt"))
