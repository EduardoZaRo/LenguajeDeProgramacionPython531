# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
import numpy as np

df = pd.read_csv("DENDOGRAMA VINITOS.csv")
df = df.set_index('PAIS')
df = df.rename_axis(None, axis = 1)#Tuve que cambiar el del porque me daba error


# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')
print(Z)

# Plot with Custom leaves
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)
plt.axis('on')
# plt.title('Clasificacion de la redes respecto a su uso')
plt.xlabel('PAISES')
plt.ylabel('Valores')
plt.savefig("DENDOGRAMA PAISES.png", dpi=600, bbox_inches='tight')
plt.show()


