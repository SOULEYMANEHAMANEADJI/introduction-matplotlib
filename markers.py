import matplotlib.pyplot as plt

# Le bloc de code suivant est commenté. Il crée un graphique avec des points marqués par des cercles.
"""
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o')
plt.show()
"""

# Définition des données pour le tracé
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 20]

# Création de plusieurs tracés avec différents marqueurs pour chaque tracé
plt.plot(x, y, marker='o', label='Circle')  # Marqueur en forme de cercle
plt.plot(x, y, marker='s', label='Square')  # Marqueur en forme de carré
plt.plot(x, y, marker='^', label='Triangle')  # Marqueur en forme de triangle
plt.plot(x, y, marker='*', label='Star')  # Marqueur en forme d'étoile

# Ajout des étiquettes pour les axes x et y
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Ajout d'une légende au tracé
plt.legend()

# Affichage du tracé
plt.show()