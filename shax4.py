total = 0
maximum = 0
minimum = 0
while(True):
    number1 = int(input('your number: '))
    if number1 == 7:
        print('Good Bye!')
        break
    total += number1
    if maximum<number1:
        maximum = number1
    elif minimum>number1:
        minimum = number1

print(total)
print(maximum)
print(minimum)