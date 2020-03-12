#ask for user input
# if it does not equal stop copying me repeat the comment
#ask for input again
#check it again for correct comment otherwise repeat

user_input = input("Hey how's it going? ").lower()
while user_input != 'stop copying me': 
    print(user_input)
    user_input = input()
print('UGH FINE YOU WIN')