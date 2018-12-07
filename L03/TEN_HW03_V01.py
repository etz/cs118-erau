import re
print("Programmed by Ethan Nadzieja, CS-118 Lesson Set 3\n\nProblem 1.")
print("Enter the current month (January - 1, Feb - 2):")
cm = int(input())*100
print("Enter the current day of the month:")
cd = int(input())
print("Enter the current year:")
cy = int(input())*10000
print("Enter the month you were born:")
bm = int(input())*100
print("Enter the day of the month you were born:")
bd = int(input())
print("Enter the year you were born:")
by = int(input())*10000
age = (cm+cy+cd)-(bm+by+bd)
print("You are", int(age/10000), "years old")
print("\nProblem 2.")
print("Enter the letter you are searching for:")
lt = input()
print("Enter the words you are trying to search: (Press enter for a new line or to stop)")
ta = int(0)
lines = []
while True:
    line = input()
    if line:
            if re.search(lt, line):
                ta = ta + 1
            lines.append(line)
    else:
        break
text = '\n'.join(lines)
print(ta, "of the words entered have the letter", lt)
