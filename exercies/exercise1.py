age = input('Whats your age? ')

if age != '':
    age = int(age)

    if age >= 18 and age < 21:
        print('You wear a wristband')
    elif age >= 21:
        print('You can drink')
    else:
        print('You are too young. Go away')

else:
    print('Please enter an age.')
