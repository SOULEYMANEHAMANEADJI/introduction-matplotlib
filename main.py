from random import randint
import matplotlib.pyplot as plt

# Génération de la liste x qui contient des nombres de 1 à 5
x = list(range(1, 6))

# Génération de la liste y qui contient 5 nombres aléatoires uniques triés dans l'intervalle [5, 100]
y = sorted(set([randint(5, 100) for _ in range(5)]))

# Les lignes suivantes sont commentées, elles créent un graphique à barres et un graphique linéaire simple
# plt.bar(x, y)
# plt.plot(x, y)
# plt.show()

# Création d'un graphique linéaire avec des marqueurs 'x' verts et une ligne en pointillés
plt.plot(x, y, marker='x', color='green', linestyle='--', label='Random Numbers')

# Ajout des étiquettes aux axes
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')

# Ajout d'un titre au graphique
plt.title('Customised line plot')

# Ajout d'une légende
plt.legend()

# Affichage du graphique
plt.show()