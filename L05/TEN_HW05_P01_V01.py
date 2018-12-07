#problem2
n = 10
for i in range(0, n):
   num = 0
   for j in range(0, i+1):
      print(num, end=" ")
      num = num + 1
   print('')

print('') #newline


#problem3
n = 10
spaces = 0
for i in reversed(range(0, n)):
   num = 0
   for x in range(0, spaces):
      print(' ', end="")
   for j in range(0, i+1):
      print(num, end=" ")
      num = num + 1
   print('')
   spaces = spaces+2

print('') #newline

#problem4
n = 10
num = 0
level = 0
numinc = level
for i in range(0, n): #row
   spaces = 3
   print('0', end='') #starting 0
   num = 0
   for j in range(0, n-1): #column
      if i > 0:
         numinc = level
         num = num + numinc
         if num > 9:
            spaces = 2
      print(spaces*' ', num, end='')#prints number
   level = level + 1
   print('')

print('') #newline

#problem5
num = 9
for i in range(1, num + 1):
    for j in range(num -  i,  0,  -1):
        print('  ', end='')
    # Print numbers
    for j in range(1, i):
        print(format(j, " "), end=''),
    for j in range(i, 0, -1):
        print(format(j, " "), end=''),
    print('')

print('') #newline

#problem6
num = 9
spaces = 2
for i in range(1, num + 1):
    print('')
    for j in range(num -  i,  0,  -1):
        print('  ', end='')
    # Print numbers
    for j in range(1, i):
        print(format(j, " "), end='')
    for j in range(i, 0, -1):
        print(format(j, " "), end='')
for i in reversed(range(1, num+1)):
    print('')
    for x in range(0, spaces):
      print(' ', end="")
    for j in range(1, i):
      print(format(j, " "), end='')
    spaces = spaces + 2
