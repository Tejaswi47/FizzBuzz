# Creating the fizzbuzz game using python.'FizzBuzz' is given as output when number is divided by the 3 and 5.
# 'Fizz' is given as output when divided by 3. 'Buzz' is give nas output when divided by 5.
# and calculating the Fizzbuzz upto 'n' Numbers given by the user

Number = int(input("Enter the number: "))

for i in range(Number):
    if (i % 3 == 0  and i % 5 == 0):
        print('Fizzbuzz')
    elif (i % 3 == 0):
        print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)