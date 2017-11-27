a = 3
# make it bigger by 10


print(a + 10)




b = 100
# make it smaller by 7


print(b - 7)




c = 44
# please double c's value


print(c * 2)




d = 125
# please divide by 5 d's value 


print(d / 5)




e = 8
# please cube of e's value


print(e ** 3)




f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)

print(f1 > f2)

g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)

print(g2 * 2 > g1)


h = 1357988018575474
# tell if it has 11 as a divisor (pras a boolean)

if h % 11 != 0:
    print ('Oooh, 11 is not a divisor!')
else:
    print('Yeah, 11 is a divisor!')

i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

print(i1 > i2 ** 2 and i1 < i2 ** 3)



j = 1521
# tell if j is dividable by 3 or 5 (pras a boolean)

if j % 3 == 0 or j % 5 == 0:
    print(True)
else:
    print(False)


k = "Apple"
#fill the k variable with its cotnent 4 times

k *= 4
print(k)
