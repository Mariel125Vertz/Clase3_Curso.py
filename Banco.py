class Banco:
    def  __init__(self, account, balance) :
        self.account=account
        self.balance=balance
        self._active=True

    def deposito (self, amount):
        if self._active:
            self.balance += amount
            print(f"Se a depositado {amount}. Saldo actual  {self.balance}")
        else:
            print("UPPS! PARESE QUE TU CUENTA ESTA INACTIVA, NO SE PUEDE DEPOSITAR")
    
    def withdraw (self, ammount):
        if self._active:
            if ammount  >=self.balance:
                self.balance -=ammount
                print(f"SE HA RETIRADO {ammount}. Saldo actual {self.balance}")

    def deactive_account (self):
        self.   _active = False
        print(f"LA CUENTA HA SIDO DESACTIVADA ")

    def active_account (self):
        self._active = True
        print(f"LA CUENTA HA SIDOACTIVADA ")

#LLAMAR A LOS METODOS
accouunt1=Banco("ANA", 500)
accouunt2=Banco("MARTHA", 30)

accouunt1.deposito(200)
accouunt2.deposito(300)
accouunt1.deactive_account()
accouunt1.deposito(50)

