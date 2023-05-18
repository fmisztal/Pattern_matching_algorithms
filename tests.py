import kmp_search
import kr_search
import naive_search
import random
import string


if __name__ == '__main__':

    print("--- NAIVE SEARCH ---")

    print("Empty String: ")
    pattern = " "
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if naive_search.find_n(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")



    print("\nEmpty Text: ")
    pattern = "acacagt"
    text = ""
    if naive_search.find_n(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")


    print("\nEmpty String and text: ")
    pattern = ""
    text = ""
    if naive_search.find_n(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString equal to text: ")
    pattern = "acacagt"
    text = "acacagt"
    if naive_search.find_n(pattern, text) == [0]:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString longer than text: ")
    pattern = "acacagtahehahe"
    text = "acacagt"
    if naive_search.find_n(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString not in text: ")
    pattern = "1234"
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if naive_search.find_n(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    text_1 = "Ala ma kota, a kot ma Ale."
    pattern_1 = "kot"
    expected_output_1 = [7, 15]
    print("\nValidation text 1: ")
    if naive_search.find_n(pattern_1, text_1) == expected_output_1:
        print("SUCCESS")
    else:
        print("ERROR")

    text_2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
             "Vestibulum vitae mauris id est fermentum malesuada. " \
             "Nulla eu tellus eget velit porta hendrerit. Curabitur " \
             "faucibus ante eget lectus auctor efficitur. Pellentesque " \
             "quis neque facilisis, efficitur velit ut, semper ligula. " \
             "Maecenas varius odio vel lacus maximus interdum. Mauris quis " \
             "ex id mi dignissim suscipit ut in eros. Nunc auctor, dui in " \
             "lacinia fringilla, ex ipsum ultrices risus, vel vestibulum quam " \
             "magna vitae neque. Sed tincidunt tortor nec finibus ultricies. " \
             "Morbi scelerisque congue tempor. Curabitur rutrum urna quis magna " \
             "venenatis efficitur. Vivamus ac lobortis quam. Sed viverra tortor " \
             "ligula, vel bibendum felis lacinia vel. Praesent eleifend pellentesque " \
             "enim a dignissim. Nulla facilisi."
    pattern_2 = "vel"
    expected_output_2 = [130, 252, 298, 442, 665, 692]
    print("\nValidation text 2: ")
    if naive_search.find_n(pattern_2, text_2) == expected_output_2:
        print("SUCCESS")
    else:
        print("ERROR")

    text_3 = "In hac habitasse platea dictumst. Sed porttitor tortor eget " \
             "felis scelerisque, vel placerat lorem feugiat. Nulla facilisi. " \
             "Sed vitae mi ut neque gravida lacinia vel id nunc. Vestibulum " \
             "vitae fermentum quam. Aliquam pharetra feugiat diam non fringilla. " \
             "Suspendisse vitae mi quam. Morbi faucibus sapien ut nisl gravida " \
             "lobortis. Ut iaculis auctor dolor in interdum. Pellentesque habitant " \
             "morbi tristique senectus et netus et malesuada fames ac turpis egestas. " \
             "Donec vitae mi ac elit faucibus rhoncus. Etiam pellentesque turpis quis " \
             "turpis condimentum, eget vestibulum tellus congue. Curabitur lobortis " \
             "accumsan massa, a efficitur lacus feugiat sed. Nam et justo purus. Duis " \
             "eget semper tellus, ac pharetra ipsum. Nulla vel leo semper, consectetur " \
             "tortor at, euismod ante. Nulla pellentesque varius fringilla. Sed ut consequat velit."
    pattern_3 = "ut"
    expected_output_3 = [136, 301, 811]
    print("\nValidation text 3: ")
    if naive_search.find_n(pattern_3, text_3) == expected_output_3:
        print("SUCCESS")
    else:
        print("ERROR")



    print("\n--- KR SEARCH ---")
    q = 101

    print("Empty String: ")
    pattern = " "
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if kr_search.find_kr(pattern, text, q) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nEmpty Text: ")
    pattern = "acacagt"
    text = ""
    if kr_search.find_kr(pattern, text, q) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nEmpty String and text: ")
    pattern = ""
    text = ""
    if kr_search.find_kr(pattern, text, q) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString equal to text: ")
    pattern = "acacagt"
    text = "acacagt"
    if kr_search.find_kr(pattern, text, q) == [0]:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString longer than text: ")
    pattern = "acacagtahehahe"
    text = "acacagt"
    if kr_search.find_kr(pattern, text, q) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString not in text: ")
    pattern = "1234"
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if kr_search.find_kr(pattern, text, q) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nKR and NAIVE comparison")
    kr_search.d = 2
    flag = True
    for i in range(100):
        text = ''.join(random.choices(['a', 'b'], k=100))
        pattern = ''.join(random.choices(['a', 'b'], k=10))
        if naive_search.find_n(pattern, text) != kr_search.find_kr(pattern, text, q):
            flag = False
    if flag:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\n---KMP SEARCH ---")

    print("Empty String: ")
    pattern = " "
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if kmp_search.find_kmp(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nEmpty Text: ")
    pattern = "acacagt"
    text = ""
    if kmp_search.find_kmp(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nEmpty String and text: ")
    pattern = ""
    text = ""
    if kmp_search.find_kmp(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString equal to text: ")
    pattern = "acacagt"
    text = "acacagt"
    if kmp_search.find_kmp(pattern, text) == [0]:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString longer than text: ")
    pattern = "acacagtahehahe"
    text = "acacagt"
    if kmp_search.find_kmp(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nString not in text: ")
    pattern = "1234"
    text = "asfacacagtasdacacacacagtagtacacagtdssafegs"
    if kmp_search.find_kmp(pattern, text) == []:
        print("SUCCESS")
    else:
        print("ERROR")

    print("\nKMP and NAIVE comparison")
    flag = True
    for i in range(100):
        text = ''.join(random.choices(['a', 'b'], k=100))
        pattern = ''.join(random.choices(['a', 'b'], k=10))
        if naive_search.find_n(pattern, text) != kmp_search.find_kmp(pattern, text):
            flag = False
    if flag:
        print("SUCCESS")
    else:
        print("ERROR")