class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = {}
        self.attrs = {}

    def agregar_vecino(self, nodo, peso=1):
        self.vecinos[nodo] = peso

    def obtener_vecinos(self):
        return self.vecinos

    def obtener_valor(self):
        return self.valor

    def obtener_peso_vecino(self, nodo):
        return self.vecinos.get(nodo, float('inf'))

    def eliminar_vecino(self, nodo_vecino):
        """
        Elimina un vecino del diccionario de vecinos del nodo.
        """
        if nodo_vecino in self.vecinos:
            del self.vecinos[nodo_vecino]

    def __str__(self):
        vecinos_str = ", ".join([f"{n.obtener_valor()}" for n in self.vecinos.items()])
        return f"Nodo({self.valor})------>[{vecinos_str}]"
