class ContaBancaria:
    
    def __init__(self, saldo):
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return print("Saldo insuficiente", self.saldo)
        
    def get_saldo(self):
        return self.saldo
    
contaFelipe = ContaBancaria(1000)
contaFelipe.sacar(500)