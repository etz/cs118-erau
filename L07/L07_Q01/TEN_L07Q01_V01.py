#Problem 1
def postal(first, last, addr, city, state, zi):
    array = [first, last, addr, city, state, zi]
    print(array[0], array[1])
    print(array[2])
    print(array[3], end=", ")
    print(array[4], array[5])

#Problem 2
def date(wday, month, day, year):
    print(wday[0:3], end=", ")
    print(month[0:3], end=" ")
    print(day, end=", ")
    print(year, end=" ")

#Problem 3
def convert(f):
    c = (f-32)*5/9
    print(c)
    
def table():
    f = [-22, -4, 14, 32, 59, 68, 86, 104]
    c = [-30, -20, -10, 0, 10, 20, 30, 40]
    print("  F       C")
    for x in range(0, len(f)):
        space = 2
        if f[x] > 0:
            if f[x] < 10:
                space = space + 2
            elif f[x] > 99:
                space = space - 2
            elif f[x] < 99 and f[x] > 10:
                space = 1
        if f[x] < 0:
            space = space - 1
            if f[x] < -10:
                space = space - 2
        print(" "*space,f[x],end="   ")
        space = 2
        if c[x] > 0:
            if c[x] < 10:
                space = space + 2
            elif c[x] > 99:
                space = space - 2
            elif c[x] < 99 and c[x] >= 10:
                space = 1
        if c[x] < 0:
            space = space - 1
            if c[x] <= -10:
                space = space - 2
        print(" "*space,c[x], end="")
        print("")

#Problem 4
def electionResults(party, votes):
    x = len(party)
    total = 0
    for a in range(0,x):
        total = total + votes[a]
    for y in range(0, x):
        spaces = 24-len(party[y])
        spc2 = 5
        per = round((votes[y]/total)*100, 2)
        print(party[y], " Party", " "*spaces, votes[y], " "*spc2, per, "%")


#Problem 5
def countword(filepath, search):
    x = 0
    wc = 0
    file = open(filepath, "r")
    words = file.read()
    while x < len(words):
        length = len(search)
        if words[x] == search[length-length]:
            nlength = length - 1
            if words[x+1] == search[length-nlength]:
                nlength = nlength - 1
                if words[x+2] == search[length-nlength]:
                    nlength = nlength - 1
                    if words[x+3] == search[length-nlength]:
                        wc = wc + 1
        x = x + 1
    print(wc)


#Problem 6
def bldcount(filepath):
    x = 0
    bloodtype = [0, 0, 0, 0, 0]
    file = open(filepath, "r")
    text = file.read()
    while x < len(text):
        if text[x:x+2] == "A ":
            bloodtype[0] += 1
        elif text[x:x+2] == "B ":
            bloodtype[1] += 1
        elif text[x:x+2] == "AB":
            bloodtype[2] += 1
        elif text[x:x+2] == "O ":
            bloodtype[3] += 1
        elif text[x:x+2] == "OO":
            bloodtype[4] += 1
        x += 1
    if bloodtype[0] > 0:
        print("There are", bloodtype[0], "patients with blood type A.")
    if bloodtype[1] > 0:
        print("There are", bloodtype[1], "patients with blood type B.")
    if bloodtype[2] > 0:
        print("There are", bloodtype[2], "patients with blood type AB.")
    if bloodtype[3] > 0:
        print("There are", bloodtype[3], "patients with blood type O.")
    if bloodtype[4] > 0:
        print("There are", bloodtype[4], "patients with blood type OO.")

#Problem 7
def log():
    log = open("logfile.txt", "a")
    log.write("Processing complete, ending program normally.")


#Problem 8
def quote(filepath, line):
    file = open(filepath, "r")
    lines = file.readlines()
    print(lines[line])

#Problem 11
'''

1 - name 'a' is not defined
2 - domain error
3 - name 'x' is not defined
4 - [Errno 2] No such file or directory: 'filename'

'''
