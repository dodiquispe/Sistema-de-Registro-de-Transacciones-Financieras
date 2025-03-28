from CuentaBancaria import CuentaBancaria

cuenta = CuentaBancaria("Carlos López", 1000)
cuenta.depositar(300)
cuenta.retirar(200)
cuenta.retirar(1500)  # Fallará por saldo insuficiente.
cuenta.mostrar_saldo()
cuenta.mostrar_movimientos()