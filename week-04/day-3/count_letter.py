def count_letters(string):
    letters = {}
    for index in range(len(string)):
        if not string[index] in letters:
            letters[string[index]] = 1
        else:
            letters[string[index]] += 1
    return letters