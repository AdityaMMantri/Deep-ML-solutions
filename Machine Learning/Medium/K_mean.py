import numpy as np

def euclidean_distance(point_1, point_2):
    return np.linalg.norm(np.array(point_1) - np.array(point_2))


def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    X = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):

        clusters = [[] for _ in range(k)]

        for index, point in enumerate(X):
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            centroid_idx = np.argmin(distances)
            clusters[centroid_idx].append(index)

        old_centroids = centroids.copy()

        centroids = np.array([
            X[cluster].mean(axis=0) if len(cluster) > 0 else old_centroids[i]
            for i, cluster in enumerate(clusters)
        ])

    final_centroids = [
        tuple(round(coord, 4) for coord in centroid)
        for centroid in centroids
    ]

    return final_centroids