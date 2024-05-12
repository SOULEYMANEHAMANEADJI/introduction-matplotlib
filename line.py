import matplotlib.pyplot as plt

# Définition des données pour le tracé
x, y, z = [1, 2, 3, 4, 5], [10, 15, 25, 30, 20], [5, 10, 15, 20, 25]

# La ligne suivante est commentée, elle crée un tracé de ligne avec l'étiquette 'Data line'
# plt.plot(x, y, label='Data line')

# Création d'un tracé de ligne avec l'étiquette 'Line 1'
plt.plot(x, y, label='Line 1')

# La ligne suivante est commentée, elle crée un tracé de ligne en pointillés rouge avec l'étiquette 'Dashed red line'
# plt.plot(x, y, linestyle='--', color='red', label='Dashed red line')

# Création d'un tracé de ligne en pointillés vert avec l'étiquette 'Line 2'
plt.plot(x, z, linestyle='--', color='green', label='Line 2')

# Ajout des étiquettes pour les axes x et y
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Les lignes suivantes sont commentées, elles ajoutent un titre au tracé
# plt.title('Line Plot')
# plt.title('Line Style And Color')

# Ajout d'un titre au tracé
plt.title('Multiple Line On A Single Plot')

# Ajout d'une légende au tracé
plt.legend()

# Affichage du tracé
plt.show()