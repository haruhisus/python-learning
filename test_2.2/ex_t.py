string_1, string_2, string_3 = input(), input(), input()

if "зайка" in string_1 and "зайка" in string_2 and "зайка" in string_3:
    print(min(string_1, string_2, string_3), len(min(string_1, string_2, string_3)))
elif "зайка" in string_1 and "зайка" in string_2:
    print(min(string_1, string_2), len(min(string_1, string_2)))
elif "зайка" in string_2 and "зайка" in string_3:
    print(min(string_2, string_3), len(min(string_2, string_3)))
elif "зайка" in string_1 and "зайка" in string_3:
    print(min(string_1, string_3), len(min(string_1, string_3)))
elif "зайка" in string_1:
    print((string_1), len(string_1))
elif "зайка" in string_2:
    print((string_2), len(string_2))
elif "зайка" in string_3:
    print((string_3), len(string_3))