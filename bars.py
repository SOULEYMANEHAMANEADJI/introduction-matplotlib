import matplotlib.pyplot as plt

# Définition des catégories et des valeurs pour le tracé
categories = ['Categories A', 'Categories B', 'Categories C', 'Categories D']
values = [30, 45, 20, 60]

# Création d'un graphique à barres avec des couleurs spécifiques pour chaque barre, une largeur de barre de 0.3 et une bordure noire
plt.bar(categories, values, color=['orange', 'pink', 'skyblue', 'gray'], width=0.3, edgecolor='black')

# Ajout d'un titre au graphique
plt.title('Horizontal Bar Plot')

# Ajout des étiquettes pour les axes x et y
plt.xlabel('Values')
plt.ylabel('Categories')

# Affichage du graphique
plt.show()