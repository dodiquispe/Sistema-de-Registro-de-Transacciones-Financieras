import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de tuplas: (fecha, tipo, monto, saldo)

    # Añade el monto al saldo y registra la transacción.
    def depositar(self, monto):
        # Completar lo siguiente: 
        # 1. actualizar saldo
        self.saldo+=monto
        # 2. añadir movimiento de deposito (fecha, tipo, monto, saldo) 
        self.movimientos.append((datetime.date.today(), "deposito", monto, self.saldo))
        # 3. Mostrar mensaje de depósito exitoso
        print("Depósito exitoso")

    def retirar(self, monto):
        # Completar lo siguiente: 
        # 1. Validar saldo, y si es insuficiente mostrar mensaje
        if self.saldo < monto:
            print("Saldo insuficiente")
            return
        # 2. Actualizar saldo
        self.saldo-=monto
        # 3. Añadir movimiento de retiro (fecha, tipo, monto, saldo) 
        self.movimientos.append((datetime.date.today(), "retiro", monto, self.saldo))
        # 4. Mostrar mensaje de retiro exitoso
        print('Retiro exitoso')

    def mostrar_saldo(self):
        # Completar lo siguiente: 
        # 1. mostrar mensaje con nombre de titular y su saldo.
        print(f'titular:{self.titular} \n saldo: {self.saldo}')

    def mostrar_movimientos(self):
        print(f"\n--- Historial de {self.titular} ---")
        # Completar lo siguiente: 
        # 1. iterar la lista de movimientos y mostar la fecha, tipo el monto y el saldo.
        for i in self.movimientos:
            print(f"Fecha: {i[0]} \n Tipo: {i[1]} \n Monto: {i[2]} \n Saldo: {i[3]}")
        print(self.movimientos)
