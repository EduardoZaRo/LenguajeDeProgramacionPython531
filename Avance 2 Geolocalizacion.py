import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cbook as cbook
G = nx.Graph()

#País -> Coordenadas decimales del pais -> Promedio -> Precio
G.add_node('Alemania', pos = (	10.451526,51.165691	), promedio = 	90	, precio = 	42.3	)
G.add_node('Argentina', pos = (	 	-63.616672, -38.416097 	), promedio = 	87	, precio = 	36.4	)
G.add_node('Armenia', pos = (	 45.038189, 40.069099 	), promedio = 	88	, precio = 	14.5	)
G.add_node('Australia', pos = (	 133.775136, -25.274398 	), promedio = 	89	, precio = 	35.3	)
G.add_node('Austria', pos = (	 14.550072, 47.516231 	), promedio = 	90	, precio = 	30.8	)
G.add_node('Bosnia', pos = (	 17.679076, 43.915886 	), promedio = 	87	, precio = 	12.5	)
G.add_node('Brasil', pos = (	-55,-10	), promedio = 	85	, precio = 	23.8	)
G.add_node('Bulgaria', pos = (	25.48583,42.733883	), promedio = 	88	, precio = 	14.6	)
G.add_node('Canada', pos = (	-95.0000000, 60.0000000	), promedio = 	89	, precio = 	35.7	)
G.add_node('Chile', pos = (	-71.0000000, -30	), promedio = 	87	, precio = 	20.8	)
G.add_node('China', pos = (	104.195397, 35.86166	), promedio = 	89	, precio = 	18	)
G.add_node('Chipre', pos = (	33.429859, 35.126413	), promedio = 	87	, precio = 	16.3	)
G.add_node('Croacia', pos = (	15.2, 45.1	), promedio = 	87	, precio = 	25.5	)
G.add_node('Egipto', pos = (	30.802498, 26.820553	), promedio = 	84	, precio = 	0	)
G.add_node('Eslovaquia', pos = (	19.5000000, 48.6667000	), promedio = 	87	, precio = 	16	)
G.add_node('Eslovenia', pos = (	15.0000000, 46	), promedio = 	88	, precio = 	24.8	)
G.add_node('Espana', pos = (	-3.7, 40.46	), promedio = 	87	, precio = 	28.2	)
G.add_node('Francia', pos = (	2.0000000, 46	), promedio = 	89	, precio = 	41.1	)
G.add_node('Georgia', pos = (	43.356892, 42.315407	), promedio = 	88	, precio = 	19.3	)
G.add_node('Grecia', pos = (	22.0000000, 39	), promedio = 	88	, precio = 	22.3	)
G.add_node('Hungria', pos = (	19.503304,47.162494	), promedio = 	93	, precio = 	40.6	)
G.add_node('India', pos = (	78.96288, 20.593684	), promedio = 	90	, precio = 	13.3	)
G.add_node('Inglaterra', pos = (	-2, 54	), promedio = 	92	, precio = 	51.7	)
G.add_node('Israel', pos = (	34.851612, 31.046051	), promedio = 	90	, precio = 	31.8	)
G.add_node('Italia', pos = (	12.56738, 41.87194	), promedio = 	89	, precio = 	39.7	)
G.add_node('Libano', pos = (	35.862285, 33.854721	), promedio = 	88	, precio = 	30.7	)
G.add_node('Luxemburgo', pos = (	6.129583, 49.815273	), promedio = 	88	, precio = 	23.3	)
G.add_node('Macedonia', pos = (	21.745275, 41.608635	), promedio = 	87	, precio = 	15.6	)
G.add_node('Marruecos', pos = (	-5.0000000, 32	), promedio = 	89	, precio = 	19.5	)
G.add_node('Mexico', pos = (	-102.552784,23.634501	), promedio = 	85	, precio = 	26.8	)
G.add_node('Moldavia', pos = (	28.369885, 47.411631	), promedio = 	87	, precio = 	16.7	)
G.add_node('NuevaZelanda', pos = (	174.885971, -40.900557	), promedio = 	88	, precio = 	26.9	)
G.add_node('Peru', pos = (	-76, -10	), promedio = 	84	, precio = 	18.1	)
G.add_node('Portugal', pos = (	-9.13333, 38.71667	), promedio = 	88	, precio = 	26.2	)
G.add_node('RepublicaCheca', pos = (	15.5000000, 49.7500000	), promedio = 	87	, precio = 	24.3	)
G.add_node('Rumania', pos = (	25, 46	), promedio = 	86	, precio = 	15.2	)
G.add_node('Serbia', pos = (	21, 44	), promedio = 	88	, precio = 	24.5	)
G.add_node('Sudafrica', pos = (	22.937506, -30.559482	), promedio = 	90	, precio = 	24.7	)
G.add_node('Suiza', pos = (	8.227512, 46.818188	), promedio = 	89	, precio = 	85.3	)
G.add_node('Turquia', pos = (	35, 39	), promedio = 	88	, precio = 	24.6	)
G.add_node('Ucrania', pos = (	31.16558, 48.379433	), promedio = 	84	, precio = 	9.2	)
G.add_node('Uruguay', pos = (	-55.765835, -32.522779	), promedio = 	87	, precio = 	26.4	)
G.add_node('USA', pos = (	-95.712891, 37.09024	), promedio = 	89	, precio = 	36.6	)


pos = nx.get_node_attributes(G, 'pos')
promedio = nx.get_node_attributes(G,'promedio')
precio = nx.get_node_attributes(G,'precio')


G.nodes(data=True)

#Elegi que el tamano de las bolitas sea el puntaje elo de la jugadora y el color sea el titulo que tienen
node_color=[float(promedio[v]) for v in G]#El color es la calificacion
node_size=[float(precio[v]) for v in G]#El tamano es el precio





cmap = plt.cm.viridis#Cambie de rango de color para adaptar al que tomaba por defecto en titulos

fig, ax = plt.subplots(figsize=(13.1 ,5))#Para los ejes
#Titulo y eje x/y
plt.title('Calificaciones y precios de vinos por pais')
plt.xlabel('Coordenadas geograficas X(0,0 es el centro del mapa)')
plt.ylabel('Coordenadas geograficas Y')

nx.draw(G, pos, font_size=5, font_color = "red", with_labels=True, node_size=node_size, node_color=node_color, edge_cmap=cmap, ax=ax)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(84,93))#Cambie el parametro de normalize porque daba error con node_color
ax.set_axis_on()
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
sm._A = []
a = plt.colorbar(sm)
a.set_label('                                      PROMEDIO                                         ')
#Para insertar el mapa, axes coord. sirve para mover el mapa de fondo por el plot
axes_coords = [0.052, 0, 0.75, 1.05]
ax_image = plt.gcf().add_axes(axes_coords)
img = plt.imread('unnamed_3.jpg')
ax_image.imshow(img, zorder = 0, alpha = 0.2) #Alpha para dar transparencia al mapa
ax_image.axis('off')
plt.show()

