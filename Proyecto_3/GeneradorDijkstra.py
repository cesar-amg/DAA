import Grafo as gr

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=50,Aristas=100)
Camino_corto,distancias, inicio=ErdosRenyi.Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraErdosRenyi_50_10', distancias, inicio)

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=300)
Camino_corto,distancias, inicio=ErdosRenyi.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraErdosRenyi_200_100', distancias, inicio)

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 50, proba = .25)
Camino_corto,distancias, inicio=Gilbert.Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGilbert_50_10', distancias, inicio)

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 200, proba = .25)
Camino_corto,distancias, inicio=Gilbert.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGilbert_200_100', distancias, inicio)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 50, distancia_max = 15)
Camino_corto,distancias, inicio=GeoSimple.Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGeoSimple_50_10', distancias, inicio)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
Camino_corto,distancias, inicio=GeoSimple.Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraGeoSimple_200_100', distancias, inicio)

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 50, Conexiones = 10)
Camino_corto,distancias, inicio=BarabasiAlbertInverso .Dijkstra(10)
Camino_corto.archivo_grafo_Dijkstra('DijkstraBarabasiAlbertInverso_50_10', distancias, inicio)

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 200, Conexiones = 20)
Camino_corto,distancias, inicio=BarabasiAlbertInverso .Dijkstra(100)
Camino_corto.archivo_grafo_Dijkstra('DijkstraBarabasiAlbertInverso_200_100', distancias, inicio)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
Camino_corto,distancias, inicio=DorogovtsevMendes.Dijkstra('10|0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraDorogovtsevMendes_50_10', distancias, inicio)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 200)
Camino_corto,distancias, inicio=DorogovtsevMendes.Dijkstra("10|0")
Camino_corto.archivo_grafo_Dijkstra('DijkstraDorogovtsevMendes_200_100', distancias, inicio)

Malla = gr.Grafo()
Malla.Malla(filas = 5, columnas=10)
Camino_corto,distancias, inicio=Malla.Dijkstra('0_0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraMalla_50_10', distancias, inicio)

Malla = gr.Grafo()
Malla.Malla(filas = 20, columnas=10)
Camino_corto,distancias, inicio=Malla.Dijkstra('0_0')
Camino_corto.archivo_grafo_Dijkstra('DijkstraMalla_200_100', distancias, inicio)
