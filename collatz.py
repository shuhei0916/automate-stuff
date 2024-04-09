def collatz(number):
    if number % 2 == 0:
        return number /2
    else:
        return 3 * number + 1
    
print(collatz(2))
print(collatz(3))

print('input number:')

try:
    number = int(input())
except:
    print('input must be integer.')
    exit(0)

while True:
    if number == 1:
        break
    number = collatz(number)
    print(number)