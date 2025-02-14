class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, saldo):
        self.saldo += saldo

    def retirar(self, saldo):
        self.saldo -= saldo
    
    def ver_saldo(self):
        return(f"El saldo de la cuenta es {self.saldo}")

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_saldo())
