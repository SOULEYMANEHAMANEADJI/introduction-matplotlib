import matplotlib.pyplot as plt
import numpy as np

# Le bloc de code suivant est commenté. Il crée un histogramme à partir d'une liste de données spécifique.
'''
data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8]
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
'''

# Le bloc de code suivant est commenté. Il crée un histogramme à partir d'un échantillon de données générées aléatoirement suivant une distribution normale.
'''
x = np.random.normal(170, 10, 250)
plt.hist(x, bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram of data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
'''

# Création d'un histogramme à partir des scores d'examen
exam_score = [65, 75, 80, 86, 90, 95, 98, 92, 100]
plt.hist(exam_score, bins=10, color='green', edgecolor='black')
plt.title("Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()