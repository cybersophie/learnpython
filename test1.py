character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was" + character_age + "years old.")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ", ")

print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")


phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
print(phrase.replace("Giraffe", "Elephant"))


print(3 * (4 + 5))
print(10 % 3)

my_num = 5
print(str(my_num) + " my favorite number")

my_num = -5
print(abs(my_num))
print(pow(3, 2))
print(max(4, 6))
print(min(4, 6))
print(round(3.2))
print(round(3.7))

from math import *

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))


name = input("Enter your name: ")
print("Hello " + name + "!")

