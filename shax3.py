while(True):
    number1 = int(input('your number: '))
    if number1 == 7:
        print('Good Bye!')
        break
    if number1>0:
        print('Number is positive')
    elif number1<0:
        print('Number is negative')
    else:
        print('Number is Zero')
        