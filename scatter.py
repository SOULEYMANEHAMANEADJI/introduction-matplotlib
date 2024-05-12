import matplotlib.pyplot as plt

# Définition des données pour le tracé
x, y = [2, 4, 5, 7, 8], [10, 15, 20, 25, 30]

# Création d'un graphique de dispersion avec des marqueurs 'o' rouges de taille 100 et des bordures noires
plt.scatter(x, y, color='red', marker='o', s=100, edgecolors='black')

# Ajout d'un titre au graphique
plt.title("Customized Scatter Plot")

# Ajout des étiquettes pour les axes x et y
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')

# Ajout d'une légende au graphique
plt.legend(['Scatter Plot'])

# Affichage du graphique
plt.show()