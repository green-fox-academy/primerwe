#1. convert the two strings to a list
#2. sort the list
#3. match each item from list1 to list2
#4. if all items from list1 has a 'pair' from list2 => the two words are anagrams 
# space-eket nem tudja összehasonlítani + kis- és nagybetű!!!

str1 = str(input("Enter the first word: "))
str2 = str(input("Enter the second word: "))

def is_anagram(str1,str2):
    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    i = 0
    isAnagrams = True

    while i < len(str1) and isAnagrams:
        if list1[i] == list2[i]:
            i += 1
        else:
            isAnagrams = False

    return isAnagrams

print("The two words are anagram?:", is_anagram(str1,str2))
