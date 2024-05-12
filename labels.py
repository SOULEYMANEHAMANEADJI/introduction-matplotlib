import matplotlib.pyplot as plt

# Définition des données pour le tracé
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]
z = [5, 10, 15, 20, 25]

# Création du premier tracé avec l'étiquette 'LINE 1'
plt.plot(x, y, label='LINE 1')

# Création du deuxième tracé avec l'étiquette 'LINE 2'
plt.plot(x, z, label='LINE 2')

# Ajout des étiquettes pour les axes x et y
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Ajout d'un titre au tracé
plt.title('Labeled Plot With Positioned Legend')

# Ajout d'une légende au tracé dans le coin supérieur gauche, avec une taille de police de 12 et sans cadre
plt.legend(loc='upper left', fontsize=12, frameon=False)

# Affichage du tracé
plt.show()
