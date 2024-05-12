# Projet de visualisation de données avec Matplotlib

Ce projet utilise la bibliothèque Matplotlib pour créer une variété de graphiques à partir de données générées aléatoirement.

## Installation

Pour exécuter ce projet, vous devez d'abord installer Python. Si vous ne l'avez pas encore fait, vous pouvez le télécharger et l'installer à partir du [site officiel de Python](https://www.python.org/downloads/).

Ensuite, vous devez installer le package Matplotlib. Vous pouvez le faire en utilisant pip :

```bash
pip install matplotlib
```

Vous aurez également besoin de NumPy pour certaines fonctionnalités :

```bash
pip install numpy
```

## Utilisation

Une fois que vous avez installé les dépendances nécessaires, vous pouvez exécuter chaque script Python individuellement pour voir les graphiques qu'ils produisent.

Voici un exemple de ce que fait un des scripts (par exemple, `line.py`) :

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]
plt.plot(x, y, label='LINE 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Labeled Plot With Positioned Legend')
plt.legend(loc='upper left', fontsize=12, frameon=False)
plt.show()

```
Ce script crée un graphique linéaire simple avec une légende. Les autres scripts du projet (`scatter.py`, `bars.py`, `histogram.py`, `subplot.py`, `...`) fonctionnent de manière similaire, en créant différents types de graphiques.
```
python line.py
```
## Auteur
#### Souleymane HAMANE ADJI

