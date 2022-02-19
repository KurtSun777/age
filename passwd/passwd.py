password = '123456'
i = 3

while True:
    pwd = input('please enter passwd: ')
    if pwd == password:
        print('log in')
        break
    else:
        i -= 1
        print('wrong, you will have', i, 'chance')
        if i == 0:
            break
        

    
