import matplotlib.pyplot as plt
import numpy as np

# Création d'un tableau numpy pour les valeurs à afficher dans le graphique à secteurs
y = np.array([35, 25, 25, 15])

# Création d'une liste pour les étiquettes de chaque secteur du graphique
myLabels = ['apple', 'orange', 'banana', 'pineapple']

# La ligne suivante est commentée, elle crée un graphique à secteurs avec un angle de départ de 90 degrés
# plt.pie(y, labels=myLabels, autopct='%1.2f%%', startangle=90)

# Création d'un graphique à secteurs sans angle de départ spécifié
plt.pie(y, labels=myLabels, autopct='%1.2f%%')

# Assure que le graphique est dessiné dans un cercle parfait
plt.axis('equal')

# Ajout d'une légende avec des paramètres spécifiques
plt.legend(loc='best', shadow=True, fontsize='small', labelspacing=0.5, borderaxespad=0., edgecolor='gray')

# Affichage du graphique
plt.show()
