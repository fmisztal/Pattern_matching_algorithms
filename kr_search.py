# d is the number of characters in the input alphabet
d = 256


def find_kr(pat, txt, prime_number):
    pattern_len = len(pat)
    text_len = len(txt)
    hashed_pattern = 0
    hashed_text = 0
    h = 1
    result = []

    if not pat or pattern_len > text_len:
        return result
    for i in range(pattern_len-1):
        h = (h*d) % prime_number

    for i in range(pattern_len):
        hashed_pattern = (d*hashed_pattern + ord(pat[i])) % prime_number
        hashed_text = (d*hashed_text + ord(txt[i])) % prime_number

    for i in range(text_len-pattern_len+1):
        if hashed_pattern == hashed_text:
            for j in range(pattern_len):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1

            if j == pattern_len:
                result.append(i)

        if i < text_len-pattern_len:
            hashed_text = (d*(hashed_text-ord(txt[i])*h) + ord(txt[i+pattern_len])) % prime_number

            if hashed_text < 0:
                hashed_text = hashed_text + prime_number
    return result

if __name__ == '__main__':
    txt = "asfacacagtasdacacacacagtagtacacagt"
    pat = "acacagt"

    q = 101

    print(find_kr(pat, txt, q))

