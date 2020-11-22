#Lotto test
import random

#Empty list
LottoNumbers = []

for i in range(0, 6):
    number = random.randint(1, 49)
    #Checking if the number has already been picked
    while number in LottoNumbers:
        number = random.randint(1, 49)

    #append lotto numbers
    LottoNumbers.append(number)

    #sort in ascending order
    LottoNumbers.sort()



#getting user input
#creating empty list
userNUmbers = []
for i in range(0, 6):
    number = int(input("Please enter  number between 1 and 49:"))
    while (number in userNUmbers or number<1 or number>50):
        print("invalid number, please try again. ")

    userNUmbers.append(number)


#creating a count
count = 0
for number in userNUmbers:
    if number in LottoNumbers:
        count += 1

print("you guessed " + str(count) + " " +  "number(s) correctly")
print("Lotto numbers are: ")
print(LottoNumbers)