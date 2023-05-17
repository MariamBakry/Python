# 1:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name+" "+first_name)

# 2:
n = int(input("Enter any integer number: "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
result = n+nn+nnn
print(result)

# 3:
print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')

# 5:
import math
r=6
volume = (4/3)*math.pi * (r**3)
print(volume)

# 6:
input('enter n')
val = 5

for i in range(val):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(val, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")