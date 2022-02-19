driving = input('do you drive? ')
if driving != 'yes' and 'no':
    print('please enter yes or no')
    raise SystemExit  # stop the code

age = input('how old are you? ')

if driving == 'yes':
    if int(age) >= 18:
        print('you passed!!!')
    else:
        print('how can you drive!!!')
elif driving == 'no':
    if int(age) >=18:
        print('you can have a licence')
    else:
        print('wait for few years')


