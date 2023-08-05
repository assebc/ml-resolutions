def get_median(input_list):
    array = sorted(input_list)

    mid_idx = int(len(array) / 2)
    if len(array) % 2 == 1:
        return array[mid_idx]
    else: 
        return (array[mid_idx - 1] + array[mid_idx]) / 2

def get_mode(input_list):
    frequencies = dict()

    for elem in input_list:
        if elem in frequencies:
            frequencies[elem] += 1
        else:
            frequencies[elem] = 1

    return max(frequencies, key=frequencies.get)


def get_rest(input_list, t=1.96):
    mean = sum(input_list) / len(input_list)
    sample_var =  sum([(elem - mean) ** 2 for elem in input_list]) / (len(input_list) - 1)
    sample_std = sample_var ** 0.5
    stderror = t * (sample_std / len(input_list) ** 0.5)
    conf_intervals = [mean - stderror, mean + stderror]
    return mean, sample_var, sample_std, conf_intervals

def get_statistics(input_list):
    median = get_median(input_list)
    mode = get_mode(input_list)
    mean, sample_variance, sample_standard_deviation, mean_confidence_interval = get_rest(input_list)
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }