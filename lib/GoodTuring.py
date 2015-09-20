from __future__ import division

# probability of unknown
def unknown_probability(singletonCount, totalCount):
    probability = float(singletonCount / totalCount)
    return probability


# adjust probability of singletons to account for unknown
def discount_probability(singletonCount, totalCount):
    c_smoothed = 2 * (1 / singletonCount)
    probability = float(c_smoothed / totalCount)
    return probability