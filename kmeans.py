import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm

import pandas as pd
import numpy as np

from Voronoi import Voronoi
from Centroids import Centroids

iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
print(iris.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']

plt.figure(figsize=(14,7))

colormap = np.array(['red','lime','black'])

x1 = x[['Petal_Length', 'Petal_Width']]
x2 = x[['Sepal_Length', 'Sepal_Width']]

model1 = KMeans(n_clusters=3, init='random')
model1.fit(x1)

points = x1.values.tolist()
#print(points)
vp = Voronoi(points)
vp.process()            

vertices = vp.return_voronoi_vertices()
#print(vertices)

c = Centroids(vertices, 3)
sorted_vertices = c.sort_vertices()
centroids = c.compute_centroids(sorted_vertices)

C =[]

for c in centroids:
    cc = list(c)
    C.append(cc)

CC = np.array(C)
#C = np.array([[1.7,0.2],[1.6,0.4],[1.5,0.2]])
model2 = KMeans(n_clusters=3, init=CC, n_init=1)
model2.fit(x1)

model3 = KMeans(n_clusters=3, init='random')
model3.fit(x2)

points = x2.values.tolist()
#print(points)
vp = Voronoi(points)
vp.process()            

vertices = vp.return_voronoi_vertices()
#print(vertices)

c = Centroids(vertices, 3)
sorted_vertices = c.sort_vertices()
centroids = c.compute_centroids(sorted_vertices)

C =[]

for c in centroids:
    cc = list(c)
    C.append(cc)

CC = np.array(C)
#C = np.array([[1.7,0.2],[1.6,0.4],[1.5,0.2]])
model4 = KMeans(n_clusters=3, init=CC, n_init=1)
model4.fit(x2)


plt.subplot(2,2,1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model1.labels_], s=10)
plt.title('Petal')

plt.subplot(2,2,2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model2.labels_], s=10)
plt.title('Petal')

plt.subplot(2,2,3)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[model3.labels_], s=10)
plt.title('Sepal')

plt.subplot(2,2,4)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[model4.labels_], s=10)
plt.title('Sepal')

plt.show()

