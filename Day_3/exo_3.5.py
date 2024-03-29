name1, name2 = input('Enter the first name: '), input('Enter the second name: ')
gather = (name1+name2).lower()
true = sum([gather.count(t) for t in 'True'.lower()])
love = sum([gather.count(t) for t in 'Love'.lower()])

score = int(str(true) + str(love))

if score < 10 or score > 90 :
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50 :
    print(f'Your score is {score}, you are alright together.')
else: print(f'Your score is {score}.')