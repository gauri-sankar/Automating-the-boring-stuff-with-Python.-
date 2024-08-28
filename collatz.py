def collatz(number):
    type = number % 2

    if type == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number +1

try:
    collatzvalue = int(input('\nEnter any number:'))    
    while True:
        if collatzvalue == 1:
            break
        
        collatzvalue = collatz(collatzvalue)
except ValueError: print('\nInteger only!')
