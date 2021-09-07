#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pylab import figure
import pylab
import networkx as nx
import pickle
from random import randint
import matplotlib.pyplot as plt
import numpy as np
G=nx.read_weighted_edgelist('Continentes promedio.txt', create_using=nx.MultiGraph())#Este es el grafo de continentes-paises
F=nx.read_weighted_edgelist('Valores redondeados vinitos.txt', create_using=nx.Graph())#Este es el grafo de paises-promedios

custom_node_color={}
custom_node_color['0'] = 'black'

#El codigo se ejecuta una vez por grafo, sino se sobreponen. No pude automatizarlo :(


#nx.draw(G,pos = nx.spring_layout(G,k=0.17,iterations=20), node_size = [G.degree(i) * 100 for i in G.nodes()], with_labels = True, font_size = 9)
#plt.savefig("G.png", dpi=300)
#nx.draw(F,pos = nx.spring_layout(F,k=0.17,iterations=20), node_size = [F.degree(i) * 100 for i in F.nodes()], with_labels = True, font_size = 9)
#plt.savefig("F.png", dpi=300)


#Archivo con el dato del promedio del grado de clusterizacion por nodo
avg_node_degree = nx.average_neighbor_degree(G)
vString = str(avg_node_degree)

def make_histogram(aGraph):
    fig = pylab.figure()
    hist = nx.degree_histogram(aGraph)
    pylab.bar(range(len(hist)), hist, align = 'center')
    pylab.xlim((0, len(hist)))
    pylab.xlabel("Grado del nodo")
    pylab.ylabel("Num. de Nodos")
    return fig
def save_histogram(aGraph, filename):
    fig = make_histogram(aGraph)
    fig.savefig(filename)


save_histogram(G,"CONTINENTES promedio.png")
pylab.show()
save_histogram(F,"CALIFICACIONES.png")
pylab.show()


