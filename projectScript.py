one = 0
two = 0
three = 0
four = 0
five = 0

for x in range(100):
    if x % 20 == 0:
        five += 1
    elif x % 11 == 0:
        four += 1
    elif x % 7 == 0:
        three += 1
    elif x % 3 == 0:
        two += 1
    else:
        one += 1
        
print(five)
print(four)
print(three)
print(two)
print(one)