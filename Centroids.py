from scipy.spatial import distance

class Centroids:
    def __init__(self, vertices, k):
        self.vertices = vertices
        self.k = k

    def sort_by_radius(self, item):
        return item[1][0]
        
    def sort_vertices(self):
        sorted_vertices = dict()
        sorted_vertices = dict(sorted(self.vertices.items(), key=self.sort_by_radius, reverse=True))
        return sorted_vertices

    def remove_violation_points(self, v, Test):
        vp = []
        for i in range(len(Test)):
            for j in range(i+1, len(Test)):
                if distance.euclidean(Test[i], Test[j])<self.vertices[v][0]:
                    vp.append(Test[j])

        for p in vp:
            if p in Test:
                Test.remove(p)

        return Test

    def add_centroid_points(self, Ccenter, Test, v):
        Temp=[]
        for j in range(len(Ccenter)):
            for k in range(len(Test)):
                if distance.euclidean(Ccenter[j], Test[k])<self.vertices[v][0]:
                    Temp.append(Test[k])

        for p in Temp:
            if p in Test:
                Test.remove(p)

        Ccenter = Ccenter+Test
        return Ccenter
                    
    def compute_centroids(self, sorted_vertices):
        Test = []
        Ccenter = []
        for v in sorted_vertices.keys():
            for p in sorted_vertices[v][1]:
                Test.append(tuple(p))
            
            Test = self.remove_violation_points(v, Test)
            if not Ccenter:
                Ccenter = Test
                if len(Ccenter)==self.k:
                    return Ccenter
                else:
                    Test = []
                    continue
            Ccenter = self.add_centroid_points(Ccenter, Test, v)
            if len(Ccenter)==self.k:
                return Ccenter
            else:
                Test=[]
        
        
