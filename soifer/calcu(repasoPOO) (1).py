# para q algo sea self tiene q ser de la misma clase... self se usa para variables q son de la clase
# hacemos un constructor, q va ser una variable q la voy a usar cualquier momento de la clase... 


class mi_calculadora:
    # responde pregunta sobre self... se usa solo en variables q son de mi clase
    # en este caso; self.var1 y self.var2 las puedo usar en cualquier lado de mi clase
    def __init__(self,):
        # estas son dos variables de clase, viven durante toda la clase... 
        self.var1 = 5
        self.var2 = 1

    def sumar_vars(self,):
        return self.var1 + self.var2

    # podemos crear nuestra propia excepcion...
    # en el metodo sumar no hace falta poner self porq una vez q se termino de usar el metodo, esas dos variables murieron, se fueron 
    def sumar(self, nro1, nro2):
        try:
            if nro1<0:   # si el numero 1 menor a cero levantame una excepcion
                raise Exception('no puedo hacer la operacion suma porq nro1 es menor a cero')
        except:
            return 'señor no puede poner un numero menor a cero en el primer digito'
        else:
            return nro1+nro2

    def restar(self, nro1, nro2):
        return nro1-nro2

    # puedo redefinir ciertas excepciones ,
    # quiero q el metodo multiplicar nro1 y nro2 sean del tipo  integer
    def multiplicar(self, nro1, nro2):
        try:
            if not type(nro1) is int:       # si nro1 no es un integer entonces
                raise TypeError('multiplicar solo acepta enteros') # levantame una excepcion del tipo TypeError
        except TypeError:
            return 'no puedo multiplicar'
        else:
            return nro1 * nro2

    def dividir(self, nro1, nro2):     # la division puede tener varias excepciones. no se puede dividir por cero, ni por letras
        n1 = nro1 - 5      # estas variables viven solo dentro del metodo... una vez q el metodo se termino de ejecutar se borran del sistema, desaparecen
        n2 = nro2 - 5
        n3 = 0
        try:
            n3 = n1/n2        
        except ZeroDivisionError:
            return 'no se puede dividir por cero'
        except NameError:
            return'no se puede dividir por una variable no definida'
        except TypeError:
            return 'hay un error en el  tipo de datos ingresados'
        else:
            return ('el resultado de la division es ' + n3)
        finally:                                 #hagas lo q hagas ejecutame esto
            self.var1 = nro1            # el valor del nro1 va seguir vivo en la variable self.var1 q es de ka misma clase... 
            print('quiero dividir')

class mapas:
    def get_item(self, mapa, item):
        try:
            return mapa[item]
        except KeyError:
            return 'no existe ese id'


## probando metodos de calculadora            
calcu = mi_calculadora()
print(calcu.dividir(2, 2))

## probando metodos de mapas
mi_mapa = mapas()
mi_mapa.get_item({'id':'234234', 'nombre': 'ruperta'}, 'id')
