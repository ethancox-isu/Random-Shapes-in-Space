import random

def randomWeightsSumAverage(n):
    # Sum Accumulator
    totalWeight = 0
    weights = []
    # iterate N times
    for i in range(0, n):
        # put another a weight into the list
        weights.append(random.random())

        # increment the total weight computed
        totalWeight += weights[-1]
                            #   ^ syntax sugar for "last element" if you're not familiar

    # This is what we'll return; we have a big list of random numbers and we need to normalize them with the sum
    normalizedWeights = []
    for weight in weights:
        # Iterate through and divide each by the total so their sum will be 1
        normalizedWeights.append(weight/totalWeight)

    return normalizedWeights

def randomWeightsIntervalSplit(n):
    rands = [random.random() for i in range(0, n-1)]
    rands.sort()

    weights = [rands[0]]
    for i in range(1, n-1):
        weights.append(rands[i]-rands[i-1])

    weights.append(1-rands[-1])
    print("generated weights:", len(weights), weights)
    return weights
