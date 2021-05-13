from time import sleep
from Easy import Easy_First

Title_file = open("Title.txt")

lines = Title_file.readlines()

for line in lines:
    print(line, end="")
    #sleep(0.3)
    
print("")
print("")

with open('Blurb.txt') as Blurb_file:

    for line in Blurb_file:
        for word in line.split():
            print(word, end = ' ')
            #sleep(0.1)

print("")
print("")

sleep(0.5)
            
print("Three gates stand before you, adventurer! Which shall you choose? (Enter the number for the corrusponding difficulty)")

print("")

print("1. Easy               2. Normal               3. Hard")


while True:
    difficulty = input()
    try:
        if int(difficulty) > 3:
            print("That is not a valid option, adventurer...")
            continue
        else:
            break
    except ValueError:
        print("That is not a valid option adventurer...")
        continue
if difficulty == '1':
    print("There is no shame in knowing one's limits...")
    print("")
    print("")
    Easy_First()
elif difficulty == '2':
    print("As the Sorceress intended...")
elif difficulty == '3':
    print("Beware, for you have selected the path of true peril...")

