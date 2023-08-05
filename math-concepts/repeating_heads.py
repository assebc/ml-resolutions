def repeating_heads(n, x):
    prob = (1 - (1 - 0.5**n)**x)
    payout = 100/prob
    return [prob*100, payout]