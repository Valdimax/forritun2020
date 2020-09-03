# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

i=0
for i in range(1, n+1):
    if i == 1:
        now = one = i
    elif i == 2:
        now = two = i
    elif i == 3:
        now = three = i
    else:
        now = one + two + three
        one, two, three = two, three, now
    print(now)