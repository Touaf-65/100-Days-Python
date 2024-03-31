scores = input('Enter student scores separed by a space (e.g. 156 178 165): ')
student_scores = [int(i) for i in scores.split(' ')]

max = student_scores[0]

for i in student_scores[1:]:
    if i > max: max = i

print(f'The highest score in the class is: {max}')