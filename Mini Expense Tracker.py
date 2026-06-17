choice = input('add(A) ,total(T) or exit(E)? ')
thisdict = {}

while choice.upper() != 'E':
    total = 0

    if choice.upper() == 'A':
        product = input('Product Name: ')
        amount = float(input('Amount: '))
        thisdict[product] = amount

    elif choice.upper() == 'T':
        for product in thisdict:
            total += thisdict[product]
        print('---All of your product---' if len(thisdict) != 0 else '---No product---')

        for product in thisdict:
            print(f'{product}: {thisdict[product]}$')
        print(f'Your total is {total}$')

    choice = input('add(A) ,total(T) or exit(E)? ')