import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0) 
labels = ['A', 'B', 'C', 'D', 'E','F']
sizes = np.random.randint(10, 100, size=6)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#AEF1E6']

# Crear gráfico de tarta
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Gráfico de Tarta con Información Aleatoria')
plt.show()
