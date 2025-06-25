import Grafo as gr
import FD_Fruchterman_Reigold as visFR
import Barnes_Hut as visBH

''' Force-directed: utilizando la disposición de un grafo mediante el algoritmo de equilibrio
 de fuerzas de Fruchterman y Reigold '''

'''grafo = gr.Grafo()
grafo.ErdosRenyi(100, 300)
visFR.Fruch_Reig(grafo)'''

'''
grafo =gr.Grafo()
grafo.ErdosRenyi(500,700)
visFR.Fruch_Reig(grafo)
'''

'''grafo =gr.Grafo()
grafo.Gilbert(100,.5)
visFR.Fruch_Reig(grafo)'''

'''
grafo =gr.Grafo()
grafo.Gilbert(500,.25)
visFR.Fruch_Reig(grafo)
'''

'''grafo =gr.Grafo()
grafo.GeoSimple(100,15)
visFR.Fruch_Reig(grafo)'''

'''
grafo =gr.Grafo()
grafo.GeoSimple(500,35)
visFR.Fruch_Reig(grafo)
'''

'''grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(100,10)
visFR.Fruch_Reig(grafo)'''

'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(500,20)
visFR.Fruch_Reig(grafo)
'''

'''grafo =gr.Grafo()
grafo.DorogovtsevMendes(100)
visFR.Fruch_Reig(grafo)'''

'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(500)
visFR.Fruch_Reig(grafo)
'''

grafo =gr.Grafo()
grafo.Malla(10,10)
visFR.Fruch_Reig(grafo)


'''grafo =gr.Grafo()
grafo.Malla(25,20)
visFR.Fruch_Reig(grafo)'''


# Force-directed: utilizando la optimización de Barnes y Hut
'''
grafo = gr.Grafo()
grafo.ErdosRenyi(100, 300)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.ErdosRenyi(500,700)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(100,.5)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.Gilbert(500,.25)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(100,15)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.GeoSimple(500,35)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(100,10)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.BarabasiAlbertInverso(500,20)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(100)
visBH.BarnesHut(grafo)
'''
'''
grafo =gr.Grafo()
grafo.DorogovtsevMendes(500)
visBH.BarnesHut(grafo)
'''

'''grafo =gr.Grafo()
grafo.Malla(10,10)
visBH.BarnesHut(grafo)'''

'''
grafo =gr.Grafo()
grafo.Malla(25,25)
visBH.BarnesHut(grafo)
'''
