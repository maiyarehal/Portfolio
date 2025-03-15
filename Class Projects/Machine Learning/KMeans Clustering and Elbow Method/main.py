from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.cluster import KElbowVisualizer
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import mode

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# TODO determine the best k for k-means
model = KMeans(n_init='auto')
visualizer = KElbowVisualizer(model, k=(1,11), timings=False)

visualizer.fit(X)

plt.xticks(range(1,11))
plt.title("K versus Distortion Score")
plt.xlabel("K Value")
plt.ylabel("Distortion Score")
plt.savefig("k_elbow")

# TODO calculate accuracy for best K
best_k = visualizer.elbow_value_
kmeans = KMeans(n_clusters=best_k, n_init='auto')
y_kmeans = kmeans.fit_predict(X)

y_kmeans_mapped = np.zeros_like(y_kmeans)
for cluster in range(visualizer.elbow_value_): 
    mask = (y_kmeans == cluster)  
    
    y_kmeans_mapped[mask] = mode(y_true[mask],keepdims=False)[0]  

accuracy = accuracy_score(y_true, y_kmeans_mapped)
print(f"Accuracy for the best K ({best_k}): {accuracy:.2f}")

# TODO draw a confusion matrix
conf_mat_final = confusion_matrix(y_true, y_kmeans_mapped)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat_final.T, annot=True, fmt='d', cmap='Blues')
plt.title(f'Confusion Matrix for K = {best_k}')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.savefig("confusion_matrix")
