max_int=0

while True:
    num_int = int(input("Input a number: ")) 
    if num_int < 0:
        break
    else:
        max_int = max(num_int, max_int)
print("The maximum is", max_int)  