def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    else:
        number = 3 * number +1
        return number
print('Enter a number')
try:
    number=int(input())
    count=0
    while number != 1:
        number=collatz(number)
        print(str(number) + ' ', end='')
        count=count+1
    print('Count=',count)
except:
    print('Ints only!')