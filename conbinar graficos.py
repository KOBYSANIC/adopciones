import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x1, y1 = np.random.rand(100), np.random.rand(100)
x2, y2 = np.random.rand(100), np.random.rand(100)
x3, y3 = np.random.rand(100), np.random.rand(100)
x4, y4 = np.random.rand(100), np.random.rand(100)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))



axs[0, 0].scatter(x1, y1, color='blue', alpha=0.6)
axs[0, 0].set_title('Scatter Plot 1')
axs[0, 0].set_xlabel('Eje X')
axs[0, 0].set_ylabel('Eje Y')

plt.figure(figsize=(12, 8))
scatter = plt.scatter(x2, y2, alpha=0.6, cmap='viridis')
plt.xlabel('Variable X', fontsize=14)
plt.ylabel('Variable Y', fontsize=14)


axs[1, 0].scatter(x3, y3, color='red', alpha=0.6)
axs[1, 0].set_title('Scatter Plot 3')   
axs[1, 0].set_xlabel('Eje X')
axs[1, 0].set_ylabel('Eje Y')

axs[1, 1].scatter(x4, y4, color='purple', alpha=0.6)
axs[1, 1].set_title('Scatter Plot 4')
axs[1, 1].set_xlabel('Eje X')
axs[1, 1].set_ylabel('Eje Y')

plt.tight_layout()
plt.show()
