#5.12
def test(number):
        check = int(number)
        if check > 0:
                print ("Positive")
        if check == 0:
                print ("Zero")
        if check < 0:
                print ("Negative")
#5.14
def mult3(number):
        for num in number:
                if int(num) % 3 == 0:
                        print(num)
#5.15
def vowels(string):
        vowels = "aeiouAEIOU"
        for letter in string:
                for check in vowels:
                        if letter == check:
                                print (string.index(letter))
#5.16
def indexes(string, char):
        lis = []
        for n in range(len(string)):
                if string[n] == char:
                        lis.append(n)
        return lis
#5.17
def doubles(array):
        for number in range(0, len(array)):
                if number != (len(array)-1):
                        if array[number] * 2 == array[number+1]:
                                print (array[number+1])
#5.18
def four_letter(array):
        words = []
        for string in array:
                count = 0
                for letter in string:
                        count = count + 1
                if count == 4:
                        words.append(array[array.index(string)])
        return words
#5.19
def inBoth(ar0, ar1):
        for value in ar0:
                for check in ar1:
                        if value == check:
                                return True
        return False
#5.20
def intersect(ar0, ar1):
        both = []
        for value in ar0:
                for check in ar1:
                        if value == check:
                                both.append(value)
        return both
#5.21
def pair(ar0, ar1, cons):
        for number in ar0:
                for sums in ar1:
                        if number + sums == cons:
                                print (number, sums, sep=" ")
#5.22
def pairSum(ar0, n):
        for number in ar0:
                for sums in ar0:
                        if number + sums == n:
                                print (ar0.index(number), ar0.index(sums), sep=" ")
