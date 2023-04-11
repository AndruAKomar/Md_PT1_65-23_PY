while True:
    you_login = input('Введи логин: ',).lower()
    
    def check_login(func):
        def decoder(login):
            if  login != 'admin':
                return print('Логин не верный')
            return func(login)
        return decoder

    @check_login
    def amount_on_account(name):
        return print(f'Hello, {name}.\nAmount on account:  500$') 
    
    amount_on_account(you_login)
    
