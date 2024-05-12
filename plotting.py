import matplotlib.pyplot as plt
import numpy as np

# Définition des points sur l'axe des x
xpoints = np.array([1, 2, 6, 8])

# Définition des points correspondants sur l'axe des y
ypoints = np.array([3, 8, 1, 10])

# Création d'un graphique de ces points avec des marqueurs 'x'
plt.plot(xpoints, ypoints, marker='x')

# Affichage du graphique
plt.show()