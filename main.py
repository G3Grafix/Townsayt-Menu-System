def product():
    print(
        '\nTshirt = 350'
        '\nLongsleeve = 380'
        '\nWarmer = 450'
        '\nPants = 550'
        '\nJersey = 320'
        '\nRaglan = 450'
       )

def services():
    print(
        '\nSublimation'
        '\nDirect to Print'
        '\nSilkscreen'
        '\nRepair'
        )

def about():
    print(
        '\nFb: Townsayt Midsayap'
        '\nEmail: twnsyt.midsayap@gmail.com'
        '\nContact no.:+63966 4234 072'
        )

customer = ''
print('\nWelcome to our Website!!')
print('\nProduct press p'
          '\nServices press s'
          '\nAbout press a')
while True:
    if customer == 'exit':
        print('\nSee you next time!')
        break
    print('\n|Type exit to exit|')
    customer = input('\nPlease a category: ')
    if customer == 'p':
        product()
        customer = input('\nPress b to Back')
    elif customer == 's':
            services()
            customer = input('\nPress b to Back')
    elif customer == 'a':
            about()
            customer = input('\nPress b to Back')
    elif customer == 'b':
                print('\nPlease a category: ')
                customer = input('\nProduct press p'
                                '\nServices press s'
                                '\nAbout press a')


