import Arista as ar
import Nodo as nd
import random
import math
import collections


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
            # Para grafos dirigidos, calculamos grado de entrada y salida
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
            self.crearNodo(n)  # Crear el nuevo nodo

            conexiones_realizadas = 0
            candidatos = self.obtener_nodos()
            random.shuffle(candidatos)

            for existente in candidatos:
                val_existente = existente.obtener_valor()

                # Evitar conectar consigo mismo y nodos ya saturados
                if val_existente == n or self.grado_nodo(val_existente) >= Conexiones:
                    continue

                # Probabilidad inversamente proporcional al grado
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


    def BFS(self, inicio):
        if inicio not in self.nodos:
            return None

        cola = collections.deque([self.nodos[inicio]])
        visitados = {inicio}
        padres = {inicio: None}
        arbol_bfs = Grafo(dirigido=True)  # Creamos un nuevo grafo dirigido para el árbol BFS

        # Añadimos el nodo inicial al nuevo grafo
        arbol_bfs.crearNodo(inicio)

        while cola:
            nodo_actual = cola.popleft()
            valor_actual = nodo_actual.obtener_valor()

            for vecino, _ in nodo_actual.obtener_vecinos().items():
                valor_vecino = vecino.obtener_valor()
                if valor_vecino not in visitados:
                    visitados.add(valor_vecino)
                    padres[valor_vecino] = valor_actual
                    cola.append(vecino)

                    # Añadimos el nodo vecino al nuevo grafo
                    arbol_bfs.crearNodo(valor_vecino)
                    # Añadimos la arista dirigida desde el padre al hijo en el árbol BFS
                    arbol_bfs.agregar_arista(valor_actual, valor_vecino)

        return arbol_bfs


    def DFS_R(self, inicio, visitados=None, arbol_dfs_r=None):
        if visitados is None:
            visitados = set()
        if arbol_dfs_r is None:
            arbol_dfs_r = Grafo(dirigido=True)
            if inicio in self.nodos:
                arbol_dfs_r.crearNodo(inicio)
            else:
                return None  # El nodo de inicio no existe

        visitados.add(inicio)
        nodo_actual = self.obtener_nodo(inicio)

        if nodo_actual:
            for vecino_obj, _ in nodo_actual.obtener_vecinos().items():
                vecino = vecino_obj.obtener_valor()
                if vecino not in visitados:
                    arbol_dfs_r.crearNodo(vecino)
                    arbol_dfs_r.agregar_arista(inicio, vecino)
                    self.DFS_R(vecino, visitados, arbol_dfs_r)

        return arbol_dfs_r


    def DFS_I(self, inicio):
        if inicio not in self.nodos:
            return None  # El nodo de inicio no existe

        visitados = set()
        stack = [inicio]

        arbol_dfs_i = Grafo(dirigido=True)
        arbol_dfs_i.crearNodo(inicio)
        visitados.add(inicio)

        while stack:
            actual = stack.pop()
            nodo_actual = self.obtener_nodo(actual)

            if nodo_actual:
                # Invertir el orden de los vecinos para emular DFS recursivo
                vecinos = sorted(
                    nodo_actual.obtener_vecinos().items(),
                    key=lambda x: x[0].obtener_valor(),
                    reverse=True
                )

                for vecino_obj, _ in vecinos:
                    vecino = vecino_obj.obtener_valor()
                    if vecino not in visitados:
                        visitados.add(vecino)
                        arbol_dfs_i.crearNodo(vecino)
                        arbol_dfs_i.agregar_arista(actual, vecino)
                        stack.append(vecino)

        return arbol_dfs_i

    def Dijkstra(self, inicio):
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return Grafo()

        # Inicializa estructuras
        distancias = {nodo.obtener_valor(): float('inf') for nodo in self.obtener_nodos()}
        distancias[inicio] = 0
        visitados = set()
        cola_prioridad = [(0, nodo_inicio)]  # (distancia, nodo)
        arbol_dijkstra = Grafo()
        arbol_dijkstra.crearNodo(inicio)

        while cola_prioridad:
            distancia_actual, nodo_actual = cola_prioridad.pop(0)
            valor_actual = nodo_actual.obtener_valor()

            if valor_actual in visitados:
                continue

            visitados.add(valor_actual)

            for vecino in nodo_actual.obtener_vecinos():
                valor_vecino = vecino.obtener_valor()
                peso = nodo_actual.obtener_peso_vecino(vecino)
                nueva_distancia = distancia_actual + peso
                # nueva_distancia = distancia_actual + 1  # Suponiendo peso 1 para las aristas

                if nueva_distancia < distancias[valor_vecino]:
                    distancias[valor_vecino] = nueva_distancia
                    cola_prioridad.append((nueva_distancia, vecino))
                    cola_prioridad.sort(key=lambda x: x[0])  # Ordenar por distancia
                    # Agregar nodo y arista al árbol de caminos más cortos
                    arbol_dijkstra.crearNodo(valor_vecino)
                    arbol_dijkstra.agregar_arista(valor_actual, valor_vecino)

        return arbol_dijkstra, distancias, inicio

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

    def archivo_grafo_Dijkstra(self, nombre_archivo, distancias, nodo_raiz):
        with open(f"{nombre_archivo}.gv", "w") as f:
            f.write(f"graph {nombre_archivo} {{\n")

        # Escribir nodos con etiquetas (Raiz o Nodo con distancia)
            for nodo in self.obtener_nodos():
                valor = nodo.obtener_valor()
                if str(valor) == str(nodo_raiz):
                    etiqueta = f"Raiz {valor}"
                else:
                    etiqueta = f"Nodo {valor} ({distancias[valor]})"
                f.write(f'    "{valor}" [label="{etiqueta}"];\n')

        # Escribir aristas con su peso como etiqueta
            for arista in self.obtener_aristas():
                origen = arista.origen.obtener_valor()
                destino = arista.destino.obtener_valor()
                peso = arista.obtener_peso()
                f.write(f'    "{origen}" -- "{destino}" [label="{peso}"];\n')

            f.write("}\n")