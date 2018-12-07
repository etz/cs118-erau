'''
Thomas Ethan Nadzieja
CS-118 / Fisher / Problem Set 8
'''
import string

#6.21
def reverse(phoneBook):
    reversePhoneBook = {}

    for key in phoneBook:
        newKey = phoneBook[key]
        reversePhoneBook[newKey] = newKey
    return reversePhoneBook

#6.22
def ticker(filename):

    companies = [] # to store company name
    ticker = [] # to store ticker symbol

    with open(filename) as f:
        tlist = [line.rstrip() for line in f]

    for line in range(0, len(tlist), 2):
        companies.append(tlist[line])

    for line in range(1, len(tlist), 2):
        ticker.append(tlist[line])

    dictionary = dict(zip(companies, ticker))

    company_name = input("Please enter a company name: ")
    if company_name in dictionary:
        message = dictionary[company_name]
    else:
        message = "Not found"
    print ("Ticker Symbol:", message)


#6.23
def mirror(word):
    if all(x for x in list(word) if x in list('bdiovwx')):
        print (word[::-1])
    else:
        print ('Invalid')

#6.24
def scaryDict(parmfilename):
    inputFile = open(parmfilename)
    resFile = open('dictonary.txt', 'w')
    stringcontent = inputFile.read()
    stringcontent = ''.join([chr for chr in stringcontent.lower() if chr in (string.ascii_letters + string.whitespace) ])
    splt_words = sorted(set(stringcontent.split()))
    for word in splt_words:
        if len(word) <= 2:
            splt_words.remove(word)
    counter = input("How many words would you like to display? Write 'all' for all: ")
    if counter == "all":
        counter = len(splt_words)
    for words in range(0, counter):
        print(splt_words[words])
#6.25
def names():
     name=[]
     fname = ""
     while True:
          fname = input("Enter the next name: ")
          if fname == '':
               break
          else:
               name.append(fname)
     for x in set(name):
          print ('There is {0} student named {1} '.format(name.count(x), x))

#6.26
def different(list):
    number = {}
    count = 0
    for sublist in list:
        for item in sublist:
            if item not in number:
                count = count+1
                number[item] = 1
    return count

#6.27
def week():
    days = ['Mo', 'Tu', 'Wed', 'Th', 'Fri', 'Sat', 'Sun']
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        inp = input("Enter day abbreviation:")
        if inp == '':
            break;
        for ab in range(0, len(days)):
            if inp == days[ab]:
                print(day[ab])

#6.28
def index(fileName, listWords):
    infile = open(fileName, 'r')
    lineList = infile.readlines()
    infile.close()
    dictionary = {}
    for word in listWords:
        for i in range(len(lineList)):
            if (word in lineList[i] or word.capitalize() in lineList[i]) and (word not in dictionary):
                dictionary[word] = [i + 1]
            elif (word in lineList[i] or word.capitalize() in lineList[i]) and (word in dictionary):
                dictionary[word] = dictionary[word] + [i + 1]
    for key in dictionary:
        print(key, end = ' ')
        for i in range(0, len(dictionary[key]) - 1):
            print(dictionary[key][i], end = ', ')
        print(dictionary[key][len(dictionary[key]) - 1], end = '')
        print('\n', end = '')
