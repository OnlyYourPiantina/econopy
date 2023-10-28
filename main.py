class eco:
    import os
    os.system('pip install colorama')
    from colorama import Fore

    def __init__(self, bal):  
        self.bal = int(bal)

    def addcash(self, vaule, silent):
        self.bal += int(vaule)
        if silent == False:
            print(Fore.YELLOW + f'{vaule}€ ' + Fore.CYAN + 'Has Been Added In Your Balance' + Fore.RESET)

    def removecash(self, vaule, silent):
        if vaule >= self.bal:
            exit(1)
        else:
            self.bal -= int(vaule)
            if silent == False:
                print(Fore.YELLOW + f'{vaule}€ ' + Fore.CYAN + 'Has Been Removed From Your Balance' + Fore.RESET)
    
    def bal(self):
        print(Fore.CYAN + 'Your Balance Is ' + Fore.YELLOW + f'{self.bal}€\n' + Fore.RESET)

    def balance(self):
        print(Fore.CYAN + 'Your Balance Is ' + Fore.YELLOW + f'{self.bal}€\n' + Fore.RESET)

cash = eco(bal=1)

cash.balance()