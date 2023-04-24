while True:
    try :
        number = input()
        number_list = []

        if number == '0':
            break

        for i in range(len(number)):
            number_list += [number[i]]
        if number_list == number_list[::-1]:
            print('yes')
        else:
            print('no')
    except:
        break
