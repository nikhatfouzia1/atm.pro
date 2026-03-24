class Phone:
    def __init__(self, balance):
        self.__balance=balance  
    def get_balance(self):
        return self.__balance
Ph=Phone(100)
print(Ph.get_balance())
