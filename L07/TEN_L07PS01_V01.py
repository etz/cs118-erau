"""
4.22
"""
def month(num):
    if num > 12 or num < 1:
        print("This number is out of range..")
    else:
        num = int(num)
        num = num - 1
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        print(months[num])

"""
4.23
"""

def average(string):
    avg = []
    wc = 1
    mean = 0
    string = str(string)
    for x in range(0, len(string)):
        if wc > len(avg):
            avg.append(0)
        if string[x] != " ":
            avg[wc-1] = avg[wc-1] + 1
        else:
            wc = wc + 1
    for x in range(0, len(avg)):
        if x > 0:
            avg[0] = avg[0] + avg[x]
    print("The average count was", end=" ")
    print(avg[0]/wc)


"""
4.24
"""

def cheer(team):
    team = str(team)
    print("How do you spell winner?")
    print("I know! I know!")
    for x in range(0, len(team)):
        print(team[x], end=" ")
        x = x+1
    print("!")
    print("And that's how you spell winner!")
    print("Go ", team, "!")

"""
4.25
"""

def vowelcount(string):
    string = str(string)
    vowels = [0, 0, 0, 0, 0]
    for x in range(0, len(string)):
        if string[x] == "a":
            vowels[0] = vowels[0] + 1
        elif string[x] == "e":
            vowels[1] = vowels[1] + 1
        elif string[x] == "i":
            vowels[2] = vowels[2] + 1
        elif string[x] == "o":
            vowels[3] = vowels[3] + 1
        elif string[x] == "u":
            vowels[4] = vowels[4] + 1
    print("a, e, i, o, and u appear, respectively,", vowels[0], vowels[1], vowels[2], vowels[3], vowels[4], "times.")

"""
4.26
"""

def crypto(filepath):
    x = 0
    file = open(filepath, "r")
    text = file.read()
    while x < len(text):
        if text[x:x+6] == 'secret':
            x = x+6
            print("xxxxxx", end="")
        print(text[x], end="")
        x = x+1

""" EXTRA CREDIT
4.28
"""

def links(filepath):
    link = 0
    x = 0
    file = open(filepath, "r")
    text = file.read()
    while x < len(text):
        if text[x:x+4] == '</a>':
            link = link + 1
        x = x + 1
    print(link)

"""
4.29
"""

def stats(filepath):
    x = 0
    wc = 0
    file = open(filepath, "r")
    lines = file.readlines()
    print("Line Count:", len(lines))
    file = open(filepath, "r")
    words = file.read()
    while x < len(words):
        if words[x] == " ":
            wc = wc + 1
        x = x + 1
    print("Word Count:", wc+len(lines))
    print("Character Count:", len(words))

"""
4.30
"""

def distribution(filepath):
    x = 0
    grades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    file = open(filepath, "r")
    text = file.read()
    while x < len(text):
        if text[x:x+2] == "A+":
            grades[0] += 1
        elif text[x:x+2] == "A ":
            grades[1] += 1
        elif text[x:x+2] == "A-":
            grades[2] += 1
        elif text[x:x+2] == "B+":
            grades[3] += 1
        elif text[x:x+2] == "B ":
            grades[4] += 1
        elif text[x:x+2] == "B-":
            grades[5] += 1
        elif text[x:x+2] == "C+":
            grades[6] += 1
        elif text[x:x+2] == "C ":
            grades[7] += 1
        elif text[x:x+2] == "C-":
            grades[8] += 1
        elif text[x:x+2] == "D+":
            grades[9] += 1
        elif text[x:x+2] == "D ":
            grades[10] += 1
        elif text[x:x+2] == "D-":
            grades[11] += 1
        elif text[x:x+2] == "F ":
            grades[12] += 1
        x += 1
    if grades[0] > 0:
        print(grades[0], " students got A+")
    if grades[1] > 0:
        print(grades[1], " students got A")
    if grades[2] > 0:
        print(grades[2], " students got A-")
    if grades[3] > 0:
        print(grades[3], " students got B+")
    if grades[4] > 0:
        print(grades[4], " students got B")
    if grades[5] > 0:
        print(grades[5], " students got B-")
    if grades[6] > 0:
        print(grades[6], " students got C+")
    if grades[7] > 0:
        print(grades[7], " students got C")
    if grades[8] > 0:
        print(grades[8], " students got C-")
    if grades[9] > 0:
        print(grades[9], " students got C+")
    if grades[10] > 0:
        print(grades[10], " students got C")
    if grades[11] > 0:
        print(grades[11], " students got C-")
    if grades[12] > 0:
        print(grades[12], " students got F")

"""
4.32
"""

def censor(filepath):
    x = 0
    file = open(filepath, "r")
    output = open("output.txt", "w")
    text = file.read()
    while x < len(text):
        if x + 4 < len(text):
            if text[x+4] == ' ':
                x = x+4
                output.write("xxxx ")
        output.write(text[x])
        x = x+1
