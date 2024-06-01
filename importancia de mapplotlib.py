import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
np.random.seed(42)
x = np.random.rand(100) 
y = np.random.rand(100) 
colors = np.random.rand(100) 
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(12, 8))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, label='Color Scale')  # Añadir barra de colores

plt.title('Utilidad de los Gráficos de Dispersión', fontsize=16)
plt.xlabel('Variable X', fontsize=14)
plt.ylabel('Variable Y', fontsize=14)

plt.figtext(0.5, 0.01, "Visualizar relaciones, Detectar patrones, Identificar anomalías, "
                       "Análisis exploratorio de datos (EDA), Visualizar variabilidad",
            wrap=True, horizontalalignment='center', fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

plt.show()
