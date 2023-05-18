def find_n(string, text):
    results = []
    if not string:
        return results
    for index in range(len(text)):
        if text[index] == string[0]:
            isFound = True
            for position in range(len(string)):
                if position + index >= len(text):
                    isFound = False
                    break
                if text[index + position] != string[position]:
                    isFound = False
                    break
            if isFound:
                results.append(index)
    return results


if __name__ == '__main__':
    print(find_n("acacagt", "asfacacagtasdacacacacagtagtacacagt"))
