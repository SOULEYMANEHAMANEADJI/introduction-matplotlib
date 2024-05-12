import matplotlib.pyplot as plt

# Création du premier sous-tracé (2 lignes, 2 colonnes, position 1)
plt.subplot(2, 2, 1)
# Tracé de [4, 5, 6] en fonction de [1, 2, 3]
plt.plot([1, 2, 3], [4, 5, 6])
# Ajout d'un titre au premier sous-tracé
plt.title("Plot 1")

# Création du deuxième sous-tracé (2 lignes, 2 colonnes, position 2)
plt.subplot(2, 2, 2)
# Tracé de [6, 5, 4] en fonction de [3, 2, 1]
plt.plot([3, 2, 1], [6, 5, 4])
# Ajout d'un titre au deuxième sous-tracé
plt.title("Plot 2")

# Création du troisième sous-tracé (2 lignes, 2 colonnes, position 3)
plt.subplot(2, 2, 3)
# Tracé de [4, 5, 6] en fonction de [1, 2, 3] en rouge
plt.plot([1, 2, 3], [4, 5, 6], color="red")
# Ajout d'un titre au troisième sous-tracé
plt.title("Red Plot")

# Création du quatrième sous-tracé (2 lignes, 2 colonnes, position 4)
plt.subplot(2, 2, 4)
# Tracé de [6, 5, 4] en fonction de [3, 2, 1] en violet
plt.plot([3, 2, 1], [6, 5, 4], color="purple")
# Ajout d'un titre au quatrième sous-tracé
plt.title("Purple Plot")

# Affichage des sous-tracés
plt.show()