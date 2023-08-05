# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_pids = find_k_nearest_neighbors(examples, features, k)
    labels = [examples[pid][label_key] for pid in k_nearest_pids]
    return round(sum(labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    distance = {}
    l = []
    for key,value in examples.items():
        d = 0
        for feature, input_feature in zip(list(value.values())[0], features):
            d += (feature - input_feature)**2

        distance[key] = [d**0.5,list(value.values())[1]]
    sorted_distance = sorted(distance.items(), key=lambda x: x[1][0])

    for i in range(k):
        l.append(sorted_distance[i][0])

    return l