class matematica:
    def sumar(self, nro1, nro2):
        return nro1+nro2

    def restar(self, nro1, nro2):
        return nro1-nro2

    def multiplicar(self, nro1, nro2):
        return nro1*nro2

    def dividir(self, nro1, nro2):
        return nro1/nro2

objeto = matematica()
print(objeto.sumar(5, 3))
print(objeto.restar(5, 3))
print(objeto.multiplicar(5, 3))
print(objeto.dividir(5, bytes))
