import matplotlib.pyplot as plt

# Définition des données pour le tracé
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Création du premier sous-tracé (1 ligne, 2 colonnes, position 1)
plt.subplot(1, 2, 1)
# Tracé de y en fonction de x
plt.plot(x, y)
# Activation de la grille
plt.grid(True)

# Création du deuxième sous-tracé (1 ligne, 2 colonnes, position 2)
plt.subplot(1, 2, 2)
# Tracé du carré de y en fonction de x
plt.plot(x, [i**2 for i in y])
# Activation de la grille
plt.grid(True)

# Le bloc de code suivant est commenté. Il crée un tracé de y en fonction de x avec une grille de couleur grise, un style de ligne en pointillés et une largeur de ligne de 0.5.
'''
plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
'''

# Affichage des tracés
plt.show()