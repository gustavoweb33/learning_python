# converting km to miles in user input
print('Enter the kms that you wish to convert to miles.')
kms = input()

miles = float(kms) / 1.609
miles = round(miles, 3)
print(f"{kms}kms  is {miles} miles")
