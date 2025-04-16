import Grafo as gr

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=50,Aristas=100)
ErdosRenyi.archivo_grafo('ErdosRenyi50')

ErdosRenyi = gr.Grafo()
ErdosRenyi.ErdosRenyi(Nodos=200,Aristas=400)
ErdosRenyi.archivo_grafo('ErdosRenyi200')

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

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 200, distancia_max = 25)
GeoSimple.archivo_grafo('GeoSimple200')

GeoSimple = gr.Grafo()
GeoSimple.GeoSimple(Nodos = 500, distancia_max = 50)
GeoSimple.archivo_grafo('GeoSimple500')


BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 50, Conexiones = 10)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso50')

BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 200, Conexiones = 20)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso200')

BarabasiAlbertInverso = gr.Grafo()
BarabasiAlbertInverso.BarabasiAlbertInverso(Nodos = 500, Conexiones = 50)
BarabasiAlbertInverso.archivo_grafo('BarabasiAlbertInverso500')

DorogovtsevMendes = gr.Grafo()
DorogovtsevMendes.DorogovtsevMendes(Nodos = 50)
DorogovtsevMendes.archivo_grafo('DorogovtsevMendes50')

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
Malla.archivo_grafo('Malla500')
