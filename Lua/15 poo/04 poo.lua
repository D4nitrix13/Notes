-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

--[[
Encapsulamiento:

El encapsulamiento implica ocultar los detalles internos de una clase y permitir el acceso solo a través de métodos definidos. En este ejemplo, la clase "CuentaBancaria" tiene métodos para depositar, retirar y consultar saldo, pero los atributos están ocultos y solo se accede a ellos a través de estos métodos.
]]

-- Definición de la clase "CuentaBancaria"
local CuentaBancaria = {
    saldo = 0,
}

-- Método para depositar dinero en la cuenta
function CuentaBancaria:depositar(monto)
    self.saldo = self.saldo + monto
    print("Depósito de", monto, "realizado.")
end

-- Método para retirar dinero de la cuenta
function CuentaBancaria:retirar(monto)
    if monto <= self.saldo then
        self.saldo = self.saldo - monto
        print("Retiro de", monto, "realizado.")
    else
        print("Fondos insuficientes.")
    end
end

-- Método para consultar el saldo de la cuenta
function CuentaBancaria:consultarSaldo()
    print("Saldo actual:", self.saldo)
end

-- Crear instancia de CuentaBancaria
local miCuenta = CuentaBancaria

-- Realizar operaciones en la cuenta
miCuenta:depositar(1000)
miCuenta:retirar(1000)
miCuenta:consultarSaldo()
miCuenta:retirar(1000)
