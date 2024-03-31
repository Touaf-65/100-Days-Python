map = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

for i in map:
    print(i,'\n')

pos = input('Enter a position(e.g. 23 for line 2, column 3) : ')

map[int(pos[0])-1][int(pos[1])-1] = 'X'

for i in map:
    print(i,'\n')