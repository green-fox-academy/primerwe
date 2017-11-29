# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

def matchMaking():
    girls = ["Eve", "Ashley", "Bozsi", "Kat", "Jane"]
    boys = ["Joe", "Fred", "Bela", "Todd", "Neef", "Jeff"]
    order = []
    x = 0
    for i in boys:
        if x < len(girls):
            order.append(girls[x])
            order.append(boys[x])
            x += 1
        else:
            print(order)
    return

print(matchMaking())


