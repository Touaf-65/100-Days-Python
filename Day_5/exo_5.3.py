print(sum([i for i in range(101) if i% 2 == 0]))

sum = 0
for i in range(101):
    if i% 2 == 0:
        sum += i
print(sum)

sum = 0
for i in range(0,101,2):
    if i% 2 == 0:
        sum += i
print(sum)