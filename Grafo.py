import Arista as ar
import Nodo as nd
import random
import math


class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = {}
        self.aristas = []
        self.posiciones = {}
        self.dirigido = dirigido

    def crearNodoGeo(self, valor, x, y):
        if valor not in self.nodos:
            self.nodos[valor] = nd.Nodo(valor)
            self.posiciones[valor] = (x, y)

    def distancia(self, nodo1, nodo2):
        x1, y1 = self.posiciones[nodo1]
        x2, y2 = self.posiciones[nodo2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def crearNodo(self, valor):
        if valor not in self.nodos:
            self.nodos[valor] = nd.Nodo(valor)
        return self.nodos[valor]

    def grado_nodo(self, valor):
        nodo = self.obtener_nodo(valor)
        if not nodo:
            return 0

        if self.dirigido:
            grado_salida = len(nodo.obtener_vecinos())
            grado_entrada = sum(1 for n in self.obtener_nodos() if nodo in n.obtener_vecinos())
            return ('Entrada=' + str(grado_entrada), 'Salida=' + str(grado_salida))
        else:
            return len(nodo.obtener_vecinos())

    def agregar_arista(self, origen, destino):
        nodo_origen = self.crearNodo(origen)
        nodo_destino = self.crearNodo(destino)

        arista = ar.Arista(nodo_origen, nodo_destino, self.dirigido)
        self.aristas.append(arista)

        nodo_origen.agregar_vecino(nodo_destino)

        if not self.dirigido:
            nodo_destino.agregar_vecino(nodo_origen)

        return arista

    def obtener_nodo(self, valor):
        return self.nodos.get(valor)

    def existe_arista(self, origen, destino):
        nodo_origen = self.obtener_nodo(origen)
        nodo_destino = self.obtener_nodo(destino)

        if not nodo_origen or not nodo_destino:
            return False

        if self.dirigido:
            return nodo_destino in nodo_origen.obtener_vecinos()

        return (nodo_destino in nodo_origen.obtener_vecinos() or nodo_origen in nodo_destino.obtener_vecinos())

    def obtener_aristas(self):
        return self.aristas

    def obtener_nodos(self):
        return list(self.nodos.values())

    def ErdosRenyi(self, Nodos, Aristas):
        for nodo in range(Nodos):
            self.crearNodo(nodo)

        i = 0
        while (i < Aristas):
            origen = random.randint(0, Nodos - 1)
            destino = random.randint(0, Nodos - 1)
            if self.existe_arista(origen, destino) == self.dirigido and origen != destino:
                self.agregar_arista(origen, destino)
                i += 1

    def Gilbert(self, Nodos, proba):
        for nodo in range(Nodos):
            self.crearNodo(nodo)

        for i in range(Nodos):
            for j in range(i + 1, Nodos):
                if random.random() < proba and self.existe_arista(i, j) == self.dirigido:
                    self.agregar_arista(i, j)

    def GeoSimple(self, Nodos, distancia_max):
        for nodo in range(Nodos):
            x = random.uniform(0, Nodos)
            y = random.uniform(0, Nodos)
            # x = random.uniform(0, base)
            # y = random.uniform(0, altura)
            self.crearNodoGeo(nodo, x, y)

        for i in range(Nodos):
            for j in range(i + 1, Nodos):
                if self.distancia(i, j) <= distancia_max and self.existe_arista(i, j) == self.dirigido:
                    self.agregar_arista(i, j)

    def BarabasiAlbertInverso(self, Nodos, Conexiones):
        for n in range(1, Nodos + 1):
            self.crearNodo(n) 

            conexiones_realizadas = 0
            candidatos = self.obtener_nodos()
            random.shuffle(candidatos)

            for existente in candidatos:
                val_existente = existente.obtener_valor()

                if val_existente == n or self.grado_nodo(val_existente) >= Conexiones:
                    continue

                Pv = 1 - (self.grado_nodo(val_existente) / Conexiones)

                if random.random() < Pv:
                    self.agregar_arista(val_existente, n)
                    conexiones_realizadas += 1

                    if conexiones_realizadas >= Conexiones:
                        break

    def BarabasiAlbert(self, Nodos, Conexiones):

        for valnodo in range(1, Nodos + 1):
            self.crearNodo(valnodo)
            for exisN in self.obtener_nodos():
                if self.grado_nodo(exisN.obtener_valor()) < Conexiones and exisN.obtener_valor() != valnodo:
                    Pv = 1 - ((self.grado_nodo(exisN.obtener_valor())) / Conexiones)
                    if random.random() < Pv:
                        self.agregar_arista(exisN.obtener_valor(), valnodo)

    def DorogovtsevMendes(self, Nodos):
        A, B, C = "0|0", "10|0", "5|10"
        self.agregar_arista(A, B)
        self.agregar_arista(B, C)
        self.agregar_arista(C, A)
        CoorNodos = []
        i = 1
        while i <= Nodos - 3:
            AristaAle = random.choice(self.obtener_aristas())
            for nodo in AristaAle.obtener_nodos():
                CoorNodos.append(nodo.obtener_valor())
            newNod = str(random.randint(-20, 20)) + '|' + str(random.randint(-20, 20))
            if self.existe_arista(newNod, CoorNodos[0]) == self.dirigido:
                self.agregar_arista(newNod, CoorNodos[0])
            if self.existe_arista(newNod, CoorNodos[1]) == self.dirigido:
                self.agregar_arista(newNod, CoorNodos[1])
            CoorNodos.pop()
            CoorNodos.pop()
            i += 1

    def Malla(self, filas, columnas):

        for i in range(filas):
            for j in range(1, columnas):
                origen = f'{i}_{j - 1}'
                destino = f'{i}_{j}'
                self.agregar_arista(origen, destino)

        for j in range(columnas):
            for i in range(1, filas):
                origen = f'{i - 1}_{j}'
                destino = f'{i}_{j}'
                self.agregar_arista(origen, destino)

    def __str__(self):
        tipo = "Dirigido" if self.dirigido else "No dirigido"
        nodos = ", ".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos())
        aristas = "\n".join(str(arista) for arista in self.obtener_aristas())

        return f"Grafo ({tipo})\nNodos: [{nodos}]\nAristas:\n{aristas}"

    def archivo_grafo(self, valor):
        f = open(str(valor + ".gv"), "w")
        f.write(str('graph ' + valor + '={\n'))
        f.write(";\n".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos()))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.obtener_aristas()))
        f.write(";\n}")
        f.close()
