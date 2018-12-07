#5.23
def pay(wage, hours):
    newhours = 0
    if hours > 60:
        update = hours - 60
        hours = hours-update
        update = update*2
        newhours = update
    if hours > 40:
        update = hours - 40
        hours = hours-update
        update = update*1.5
        newhours = newhours + update
    newhours = newhours + hours
    print(newhours * wage)

#5.24
def case(string):
    if ord(string[0]) > 64 and ord(string[0]) < 90:
        return "capitalized"
    elif ord(string[0]) > 97 and ord(string[0]) < 122:
        return "not capitalized"
    else:
        return "unknown"

#5.25
def leap(year):
    if year % 400 == 0:
        return "true"
    if year % 4 == 0 and year % 100 > 0:
        return "true"
    else:
        return "false"
#5.26
def rps(act1, act2):
    if ord(act1) == 82 or ord(act1) == 114:
        if ord(act2) == 82 or ord(act2) == 114:
            return 0
        if ord(act2) == 80 or ord(act2) == 112:
            return 1
        if ord(act2) == 83 or ord(act2) == 115:
            return -1
    if ord(act1) == 80 or ord(act1) == 112:
        if ord(act2) == 82 or ord(act2) == 114:
            return -1
        if ord(act2) == 80 or ord(act2) == 112:
            return 0
        if ord(act2) == 83 or ord(act2) == 115:
            return 1
    if ord(act1) == 83 or ord(act1) == 115:
        if ord(act2) == 82 or ord(act2) == 114:
            return -1
        if ord(act2) == 80 or ord(act2) == 112:
            return 1
        if ord(act2) == 83 or ord(act2) == 115:
            return 0

#5.27
def letter2number(letter):
    grade = 0
    if letter[0] == "A":
        grade = 4
    if letter[0] == "B":
        grade = 3
    if letter[0] == "C":
        grade = 2
    if letter[0] == "D":
        grade = 1
    if letter[1] == "-":
        grade = grade - 0.3
    if letter[1] == "+":
        grade = grade + 0.3
    return grade

#5.28
def geometric(array):
    check = 0
    array.reverse()
    sequence = array[0] / array[1]
    for number in range(0, len(array)-1):
        if array[number] / array[number+1] == sequence:
            check = check + 1
        if check >= (len(array)-1):
            return "true"
    return "false"

#5.29
def lastfirst(names):
    first = []
    last = []
    index = 0
    for name in names:
        for letter in name:
            index = index + 1
            if letter == ",":
                comma = index
                first.append(names[names.index(name)][:comma-1])
                last.append(names[names.index(name)][comma+1:])
        index = 0
    return last, first

#5.30
def many(file):
    words = []
    characters = [0,0,0,0,0,0,0,0,0,0]
    file = open(file, "r")
    lines = file.readlines()
    for line in range(0, len(lines)):
        index = 0
        for letter in lines[line]:
            if letter == " ":
                words.append(index)
                print (index)
                index = 0
            else:
                index += 1
    for number in words:
        characters[number] = characters[number] + 1
    for entry in range(0, len(characters)):
        print("Words of Length ", entry, characters[entry])

#5.31
def subsetSum(ar0, n):
        for num0 in ar0:
            for num1 in ar0:
                for num2 in ar0:
                    if num0 + num1 + num2 == n:
                        return "true"
        return "false"
#5.32
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

#5.33
def mystery(num):
    loops = 0
    while True:
        if num < 1:
            return loops-1
        num = num / 2
        loops = loops + 1

#5.34
def statement(array):
    statement = [0,0]
    for number in array:
        if number > 0:
            statement[0] = statement[0] + number
        else:
            statement[1] = statement[1] + number
    return statement

#5.35
def pixels(array):
    count = 0
    for ars in range(0, len(array)):
        for nums in range(0, len(array[ars])):
            if array[ars][nums] > 0:
                count = count + 1
    return count
