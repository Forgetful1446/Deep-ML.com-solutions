import numpy as np

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points)
    centroids = np.array(initial_centroids)

    for _ in range(max_iterations):
        distances = np.linalg.norm(points[:, None] - centroids, axis=2)
        assign = np.argmin(distances, axis=1)	

        new_centroids = []
        for i in range(k):
            cluster_points = points[assign == i]

            if len(cluster_points) == 0:
                new_centroids.append(centroids[i])
            else:
                new_centroids.append(np.mean(cluster_points, axis=0))

        centroids = np.array(new_centroids)

    return [tuple(c) for c in centroids]
