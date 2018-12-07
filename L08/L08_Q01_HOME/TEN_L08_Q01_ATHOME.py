import random


#Problem 1
def words():
    words = ["hello","mother","hello", "father", "here", "i", "am", "hello"]
    words = sorted(set(words))
    print(words)

#Problem 3
'''
        ORDERED - MUTABLE - ITERABLE - ALLOWED DUPLICATES
tuple      y    |    n    |     y    |          y
dictionary y    |    n    |     y    |          n
set        y    |    y    |     n    |          n
list       y    |    y    |     y    |          y


'''
#Problem 5
def bridgeHands():
    cards = 1
    deck = [0]
    flag = 0
    while (cards <= 52):
        deck.append(cards)
        cards = cards + 1
    random.shuffle(deck)
    for x in range(0, 4):
        multiplier = (x * 13)
        for y in range(0,12):
            if flag == 0:
                if x == 0:
                    flag = 1
                    print ("North: ", end="")
                if x == 1:
                    flag = 1
                    print ("South: ", end="")
                if x == 2:
                    flag = 1
                    print ("East: ", end="")
                if x == 3:
                    flag = 1
                    print ("West: ", end="")

            print(deck[multiplier+y], end=", ")
        print("")
        flag = 0
#Problem 6
'''
The first 128 Unicode code points are the ASCII characters. Their decimal values remain the same.
'''

#Problem #7
def heads():
    outcome = random.choice(['HEAD','TAIL'])
    heads = 0
    results = []
    while outcome != "TAIL":
        results.append(outcome)
        outcome = random.choice(['HEAD','TAIL'])
        heads = heads + 1;
    print(heads, "# Your results were: ", end="")
    for x in range(0, len(results)):
        print(results[x], end=" ")
    print("TAILS")

'''
Problem #8

def rare(n):
    res = 0
    for i in range(n):
        if heads() > 4:
            res += 1
    return res*100/n

This function will call upon the heads() function looking for a return statement
above the number 4. If it receives 4 or above, it adds one to 'res'. Res is then
multiplied by 100 and divided by the number given in the input of the function
rare(n).
'''
#Problem 9
def lottery(num):
    counter = 0
    while (counter < 6):
        rand = random.randint(0,num)
        print(rand, end="")
        counter = counter + 1
        next = input()

#Problem 11
def wordcount(filepath):
    file = open(filepath, "r")
    freq = []
    sortwordsList = []
    i = 0
    k = 0
    wordsList = file.readlines()
    for word in wordsList:
        wordsList[i] = str(word.lower())
        word.lstrip()
        word.replace(' ','').isalpha()
        i = i + 1
    for word in wordsList:
        for j in range(0,len(wordsList)):
            if (word==wordsList[j]):
                flag = 1
            if (flag != 1):
                if(len(word)>2):
                    sortwordsList.append(word)
                    k= k+1
            flag = 0
    for word in sortwordsList:
        print(word+" "+str(wordsList.count(word)))

#Problem 12
def diceprob(r):
    total_count = 0
    count = 0
    while count < 100:
        roll = random.randint(1, 6) + random.randint(1, 6)
        if roll == r:
            count += 1
        total_count += 1
    print("It took " + str(total_count) + " rolls to get 100 rolls of " + str(r))

#Problem 13
def yahtzee():
   savedDice = ""
   outcomes = []
   for i in range(1, 4):
       if i == 1:
           for i in range(0, 5):
               outcomes.append(random(1, 6));
       else:
           diceSaved = savedDice.strip().split(',')
           for j in range(0, 5):
               if str(j) not in diceSaved:
                   outcomes[j] = (random.randint(1, 6));

       print("You have ", end="")
       for k in range(0, 4):
           print(outcomes[k], end=", ")
       print("and " + str(outcomes[4]))
       if i != 3:
           savedDice = input("What dice you want to save? ")

   print("Write your score.")
