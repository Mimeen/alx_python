#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#calc last digit
last_digit = number % 10;

#when last_digit is greater than 5
if last_digit > 5:
    print("The last digit of {} is {} and is greater than 5".format(number) .format(last_digit))
elif last_digit == 0:
    print("The last digit of {} is {} and is 0".format(number) .format(last_digit))
else:
    print("The last digit of {} is {} and is less than 6 and not 0".format(number) .format(last_digit))