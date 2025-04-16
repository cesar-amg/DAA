class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = {}

    def agregar_vecino(self, nodo, peso=1):
        self.vecinos[nodo] = peso

    def obtener_vecinos(self):
        return self.vecinos

    def obtener_valor(self):
        return self.valor

    def __str__(self):
        vecinos_str = ", ".join([f"{n.obtener_valor()}" for n in self.vecinos])
        return f"Nodo({self.valor})------>[{vecinos_str}]"
