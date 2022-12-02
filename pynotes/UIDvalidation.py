for _ in range(int(input())):
    UID = input()
    UIDsort = ''.join(sorted(UID))
    dig, char = 0, 0

    if len(set(UID)) == 10:
        if UID.isalnum():
            for i in UID:
                if i.isdigit():
                    dig += 1
                    continue
                if i.isupper():
                    char += 1
            if dig >= 3 and char >= 2:
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
