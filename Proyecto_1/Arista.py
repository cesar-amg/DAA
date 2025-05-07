class Arista:
    def __init__(self, inicio, destino, dirigido=False):
        self.inicio = inicio
        self.destino = destino
        self.dirigido = dirigido

    def obtener_nodos(self):
        return (self.inicio, self.destino)

    def es_dirigida(self):
        return self.dirigido

    def __str__(self):
        direccion = "->" if self.dirigido else "--"
        return f"{self.inicio.obtener_valor()} {direccion} {self.destino.obtener_valor()}"
