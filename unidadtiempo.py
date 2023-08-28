class UnidadTiempo:
    def __init__(self, tope):
        self.valor = 0
        self.tope = tope
    
    def avanzar(self):
        if self.valor == self.tope - 1:
            self.valor = 0
        else:
            self.valor += 1

class Cronometro:
    def __init__(self):
        self.segundos = UnidadTiempo(60)
        self.minutos = UnidadTiempo(60)
        self.horas = UnidadTiempo(24)
    
    def avanzar(self):
        self.segundos.avanzar()
        if self.segundos.valor == 0:
            self.minutos.avanzar()
            if self.minutos.valor == 0:
                self.horas.avanzar()
                if self.hora.valor==24:
                    self.hora.valor=0
    
    def mostrar_tiempo(self):
        return f"{self.horas.valor:02d}:{self.minutos.valor:02d}:{self.segundos.valor:02d}"

cronometro = Cronometro()
cont = 0 
while cont < 100:
    cronometro.avanzar()
    print(cronometro.mostrar_tiempo())
    cont += 1
