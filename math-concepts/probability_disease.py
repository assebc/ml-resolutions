def probability_of_disease(accuracy, prevalence):
    prob_healthy = 1-prevalence
    num = accuracy*prevalence
    den = num + ((1-accuracy) * prob_healthy)
    prob_not_healthy = num/den

    num = accuracy*prob_healthy
    den = num + ((1-accuracy) * prevalence)
    prob_not_healthy2 = num/den
    return [100*prob_not_healthy, 100*prob_not_healthy2]