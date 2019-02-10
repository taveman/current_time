phrase_1 = {1, 21, 31, 41, 51}
phrase_2 = {2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54}
phrase_3 = set(range(1, 61)) - phrase_1 - phrase_2

phrase_structure = {
    'type_1': phrase_1,
    'type_2': phrase_2,
    'type_3': phrase_3
}
