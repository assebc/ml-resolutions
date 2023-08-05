import numpy as np
import random

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()

def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    # Write your code here.
    centroids = {i: user_feature_map[inital_centroid_users[i]] for i in range(k)}
    for _ in range(10):
        user_centroid = assign_centroids(user_feature_map, centroids)
        centroids = update_centroids(user_feature_map, centroids, user_centroid)

    return list(centroids.values())

def assign_centroids(user_feature_map, centroids):
    user_centroid = {}
    for u in user_feature_map.keys():
        f = user_feature_map[u]
        distances = {}
        for k,v in centroids.items():
            distances[k] = sum(abs(i-j) for i,j in zip(f,v))
        user_centroid[u] = min(distances, key=distances.get)
        
    return user_centroid

def update_centroids(user_feature_map, centroids, user_centroid):
    for c in centroids.keys():
        group = {u:user_feature_map[u] for u, g in user_centroid.items() if g==c}
        group_features = np.array(list(group.values()))
        centroids[c] = [group_features[:,i].mean() for i in range(group_features.shape[1])]
    return centroids