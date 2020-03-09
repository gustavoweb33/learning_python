numbers = [1, 2, 5, 7, 3]

for number in numbers:
    print(number)

##############################

times = input('How many times do i have to tell you?')
times = int(times)

for i in range(times):
    print('CLEAN YOUR ROOM')


##############################
# 4 and 13 will print unlucky
# otherwise print x is even or odd

# loop through 1 20 range(1,21)
# check if x == 4 or 13
# check if x is even x % 2 == 0
# otherwise x is odd

for x in range(1, 21):
    if x == 4 or x == 13:
        print(f'{x} is unlucky')
    elif x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
