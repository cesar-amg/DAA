import Grafo as gr

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=50,Aristas=100)
ErdosRenyi.archivo_grafo('ErdosRenyi50_100')
Camino_corto=ErdosRenyi.KruskalD()
Camino_corto.archivo_grafo('KruskalDErdosRenyi_50_100')

Camino_corto2=ErdosRenyi.KruskalI()
Camino_corto2.archivo_grafo('KruskalIErdosRenyi_50_100')

Camino_corto3=ErdosRenyi.Prim(0)
Camino_corto3.archivo_grafo('PrimErdosRenyi_50_100')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=500)
ErdosRenyi.archivo_grafo('ErdosRenyi5200_500')
Camino_corto=ErdosRenyi.KruskalD()
Camino_corto.archivo_grafo('KruskalDErdosRenyi_200_500')

Camino_corto2=ErdosRenyi.KruskalI()
Camino_corto2.archivo_grafo('KruskalIErdosRenyi_200_500')

Camino_corto3=ErdosRenyi.Prim(0)
Camino_corto3.archivo_grafo('PrimErdosRenyi_200_500')

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 50, proba = .5)
Gilbert.archivo_grafo('Gilbert50_5')
Camino_corto=Gilbert.KruskalD()
Camino_corto.archivo_grafo('KruskalDGilbert_50_5')

Camino_corto2=Gilbert.KruskalI()
Camino_corto2.archivo_grafo('KruskalIGilbert_50_5')

Camino_corto3=Gilbert.Prim(0)
Camino_corto3.archivo_grafo('PrimGilbert_50_5')

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 200, proba = .5)
Gilbert.archivo_grafo('Gilbert200_5')
Camino_corto=Gilbert.KruskalD()
Camino_corto.archivo_grafo('KruskalDGilbert_200_5')

Camino_corto2=Gilbert.KruskalI()
Camino_corto2.archivo_grafo('KruskalIGilbert_200_5')

Camino_corto3=Gilbert.Prim(0)
Camino_corto3.archivo_grafo('PrimGilbert_200_5')

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 50, distancia_max = 15)
GeoSimple.archivo_grafo('GeoSimple50_15')
Camino_corto=GeoSimple.KruskalD()
Camino_corto.archivo_grafo('KruskalDGeoSimple_50_15')

Camino_corto2=GeoSimple.KruskalI()
Camino_corto2.archivo_grafo('KruskalIGeoSimple_50_15')

Camino_corto3=GeoSimple.Prim(0)
Camino_corto3.archivo_grafo('PrimGeoSimple_50_15')

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
GeoSimple.archivo_grafo('GeoSimple200_25')
Camino_corto=GeoSimple.KruskalD()
Camino_corto.archivo_grafo('KruskalDGeoSimple_200_25')

Camino_corto2=GeoSimple.KruskalI()
Camino_corto2.archivo_grafo('KruskalIGeoSimple_200_25')

Camino_corto3=GeoSimple.Prim(0)
Camino_corto3.archivo_grafo('PrimGeoSimple_200_25')

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 50, Conexiones = 10)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbert50_10')
Camino_corto=BarabasiAlbertInverso.KruskalD()
Camino_corto.archivo_grafo('KruskalDBarabasiAlbert_50_10')

Camino_corto2=BarabasiAlbertInverso.KruskalI()
Camino_corto2.archivo_grafo('KruskalIBarabasiAlbert_50_10')

Camino_corto3=BarabasiAlbertInverso.Prim(1)
Camino_corto3.archivo_grafo('PrimBarabasiAlbert_50_10')

BarabasiAlbertInverso  = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso (Nodos = 200, Conexiones = 20)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbert200_20')
Camino_corto=BarabasiAlbertInverso.KruskalD()
Camino_corto.archivo_grafo('KruskalDBarabasiAlbert_200_20')

Camino_corto2=BarabasiAlbertInverso.KruskalI()
Camino_corto2.archivo_grafo('KruskalIBarabasiAlbert_200_20')

Camino_corto3=BarabasiAlbertInverso.Prim(1)
Camino_corto3.archivo_grafo('PrimBarabasiAlbert_200_20')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes_50')
Camino_corto=DorogovtsevMendes.KruskalD()
Camino_corto.archivo_grafo('KruskalDDorogovtsevMendes_50')

Camino_corto2=DorogovtsevMendes.KruskalI()
Camino_corto2.archivo_grafo('KruskalIDorogovtsevMendes_50')

Camino_corto2=DorogovtsevMendes.Prim('0|0')
Camino_corto2.archivo_grafo('PrimDorogovtsevMendes_50')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 200)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes_200')
Camino_corto=DorogovtsevMendes.KruskalD()
Camino_corto.archivo_grafo('KruskalDDorogovtsevMendes_200')

Camino_corto2=DorogovtsevMendes.KruskalI()
Camino_corto2.archivo_grafo('KruskalIDorogovtsevMendes_200')

Camino_corto2=DorogovtsevMendes.Prim('0|0')
Camino_corto2.archivo_grafo('PrimDorogovtsevMendes_200')

Malla = gr.Grafo()
Malla.Malla(filas = 5, columnas=10)
Malla.archivo_grafo('Malla_5_10')
Camino_corto=Malla.KruskalD()
Camino_corto.archivo_grafo('KruskalDMalla_5_10')

Camino_corto2=Malla.KruskalI()
Camino_corto2.archivo_grafo('KruskalIMalla_5_10')

Camino_corto3=Malla.Prim('0_0')
Camino_corto3.archivo_grafo('PrimMalla_5_10')

Malla = gr.Grafo()
Malla.Malla(filas = 20, columnas=10)
Malla.archivo_grafo('Malla_20_10')
Camino_corto=Malla.KruskalD()
Camino_corto.archivo_grafo('KruskalDMalla_20_10')

Camino_corto2=Malla.KruskalI()
Camino_corto2.archivo_grafo('KruskalIMalla_20_10')

Camino_corto3=Malla.Prim('0_0')
Camino_corto3.archivo_grafo('PrimMalla_20_10')

"""ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=30,Aristas=60)
ErdosRenyi.archivo_grafo('ErdosRenyi30')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=100,Aristas=200)
ErdosRenyi.archivo_grafo('ErdosRenyi100')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=500,Aristas=1000)
ErdosRenyi.archivo_grafo('ErdosRenyi500')

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 50, proba = .25)
Gilbert.archivo_grafo('Gilbert50')

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 200, proba = .05)
Gilbert.archivo_grafo('Gilbert200')

Gilbert = gr.Grafo()
Gilbert.Gilbert(Nodos = 500, proba = .02)
Gilbert.archivo_grafo('Gilbert500')

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 50, distancia_max = 15)
GeoSimple.archivo_grafo('GeoSimple50')
#print(GeoSimple)

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
GeoSimple.archivo_grafo('GeoSimple200')

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 500, distancia_max = 50)
GeoSimple.archivo_grafo('GeoSimple500')


BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 50, Conexiones = 10)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso50')
#print(BarabasiAlbertInverso)

BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 200, Conexiones = 20)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso200')

BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 500, Conexiones = 50)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso500')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes50')
#print(DorogovtsevMendes)

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 200)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes200')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 500)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes500')

Malla = gr.Grafo()
Malla.Malla(filas = 5, columnas=10)
Malla.archivo_grafo('Malla50')

Malla = gr.Grafo()
Malla.Malla(filas = 20, columnas=10)
Malla.archivo_grafo('Malla200')

Malla = gr.Grafo()
Malla.Malla(filas = 50, columnas=10)
Malla.archivo_grafo('Malla500')"""