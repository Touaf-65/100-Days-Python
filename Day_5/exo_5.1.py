heights = input('Enter student heights separed by a space (e.g. 156 178 165): ')
student_heights = [ int(i) for i in heights.split(' ')]

sum, length = 0, 0

for i in student_heights:
    sum += i
    length +=1

average = int(round(sum/length,0))

print(average)
