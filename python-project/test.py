def square(number):
    if (type(number) != int and type(number) != float):
        return None
    
    return (number * number)

print(square(2.2))

def square(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number * number

print(square(2.2))
print("{:.2f}".format(square(2.2)))  # Output: 4.84

'''
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"] 

cooldictionary = {}

for i in range(0,3):
    cooldictionary[words[i]] = definitions[i]
print(cooldictionary)

nums = [99, 20, 30, 35, 16, 49, 39, 11, 69, 48, 85, 32, 10, 47, 24, 80, 37, 21, 3, 99, 13, 11, 23, 12, 40, 50, 24, 14, 10, 62, 21, 24, 55, 57, 38, 55, 83, 63, 34, 31, 15, 26, 82, 47, 37, 14, 64, 72, 90, 39, 70, 50, 67, 61, 23, 28, 30, 13, 87, 58, 80, 62, 15, 49, 33, 7, 38, 2, 92, 76, 80, 18, 6, 25, 22, 25, 91, 9, 37, 83, 46, 98, 69, 3, 40, 6, 48, 1, 63, 51, 32, 19, 77, 74, 22, 75, 41, 19, 27, 82, 60, 6, 1, 55, 5, 71, 18, 84, 47, 16, 1, 8, 41, 6, 17, 100, 62, 36, 45, 32, 4, 33, 68, 15, 2, 92, 50, 54, 34, 12, 17, 16, 74, 95, 2, 61, 75, 12, 6, 39, 28, 18, 30, 39, 8, 34, 62, 31, 57, 8, 69, 19, 71, 70, 40, 79, 76, 96, 84, 76, 85, 4, 40, 64, 45, 11, 46, 100, 56, 9, 86, 5, 78, 81, 18, 70, 76, 46, 85, 69, 64, 88, 17, 91, 49, 93, 18, 29, 38, 42, 77, 63, 46, 32, 83, 88, 48, 68, 89, 80]

index = 0

for i in nums:
    if i == 68:
        break
    index = index + 1
    
print(index)

for i in range(1,5):
    print(i)

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
odds = set()

# create a new set called odds that holds all the odd numbers from the numbers list
for number in numbers:
    if number % 2 != 0:
        odds.add(number)

print(odds)

value = 1
power = 0

while value < 1000000000:
    value = value * 2
    power = power + 1
    
print(power)

def love():
    print("I love Python!")
    
love()

def firstletter(name):
    print("first letter: "+name[0]+"\n")

firstletter("Python")

# create a function to check the input type
def checktype(input):
    if (type(input) == int):
        print("This is an integer")
    elif (type(input) == float):
        print("This is a float")
    elif (type(input) == str):
        print("This is a string")
    else:
        print("This is not a number or string")

def appendtotuple(thetuple, value):
    thetuple = thetuple + (value,)
    return thetuple

a = 5

if a > 2:
    print("a is greater than 2")
elif a > 1:
    print("a is greater than 1")
else:
    print("a is not greater than 1 or 2")

fun = True

if fun == True:
    print("We're having fun!")
elif fun == False:
    print("This is no fun")

# check the user's input value is an even number or odd number
a = int(input("Please enter a number: "))
if a % 2 == 0:
    print("a is an even number")
else:
    print("a is an odd number")

movie = input("What's your favorite movie?: ")
print(f"Your favorite movie: {movie}")

year = int(input("What year were you born?: "))
print(type(year))
'''