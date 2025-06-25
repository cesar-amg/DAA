# DAA - Proyecto 6 "Disposición de grafos - Fruchterman y Reigold - Barnes y Hut"
El Archivo principal es el de GeneradorGrafos, ahí se llama a las clases Grafo, FD_Fruchterman_Reigold y Barnes_Hut.

  - FD_Fruchterman_Reigold: esta clase mediante el método Fruch_Reig, calcula la disposición de un grafo mediante el algoritmo de equilibrio de fuerzas de Fruchterman y Reigold (1991). O(n^2)
    
  - Barnes_Hut: esta clase mediante el método BarnesHut, calcula la disposición de un grafo utilizando la optimización de Barnes y Hut (1986). O(n log(n))

  - Grafo: a su vez llama las clases Arista y Nodo para desarrollar el Grafo.
