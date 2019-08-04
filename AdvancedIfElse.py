_author_ = "dev"

# print("Please guess a number between 1 and 10")
# guess = int(input())
#
# if guess !=5:
#     if guess < 5:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#
#     guess = int(input())
#     if guess == 5:
#         print("well done, you guessed")
#     else:
#         print("sorry, you have not guess correctly")
#
# else:
#     print("you got it the first time")

# age = int(input("how old are you?"))

#if (age >= 16) and (age <= 65):
# if 16<= age <= 65:
#     print("enjoy you day at work")
#

# if age < 16 or age > 65:
#     print("enjoy your free time")
# else:
#     print("have a good day at work")

# if not age < 18:
#     print("you can vote")
# else:
#     print("pleae come back in {0}".format(18-age))



#
# parrot = "Norwegian blue"
#
# letter = input("enter a letter")
#
# if letter in parrot:
#     print("give me an {} bob".format(letter))
# else:
#     print("I don't need that letter")

name = input("enter your name")
age = int(input("enter your age, {0}".format(name)))

if 18 < age < 31:
    print("enjoy the cool peoples cruise {0}".format(name))
else:
    print("{0}, you're too old or young, either way you can't go on the cool people's trip".format(name))

