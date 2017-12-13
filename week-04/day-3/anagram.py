def is_anagram(str1, str2):
    str1 = str.lower(str1)
    str2 = str.lower(str2)
    
    list1 = ''.join(sorted(str1))
    list2 = ''.join(sorted(str2))

    if list1.replace(" ", "") == list2.replace(" ", ""):
        return True
    else:
        return False