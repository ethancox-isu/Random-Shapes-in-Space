from random import random

# Function that takes in a set of points, a tolerance, bounds of an interval, and a number of slices to take and returns whether or not any slices in that interval have ratios with differences outside of that tolerance
def checkers_1d(points, tolerance, interval, number_of_slices):
    delta = (interval[1] - interval[0]) / number_of_slices
    print(f"Delta: {delta}")
    print(f"# intervals: {number_of_slices}")

    buckets = [[] for n in range(number_of_slices)]
    for point in points:
        bucket_i = int(point // delta)
        #print(f"point {point}, delta {delta}, bucket_i {bucket_i}")
        buckets[bucket_i].append(point)

    print("Points in buckets!")
        
    found_problem = False    
    for i in range(len(buckets)):
        point_ratio = len(buckets[i]) / len(points)
        length_ratio = delta / (interval[1] - interval[0])
        difference = point_ratio - length_ratio

        if abs(difference) > tolerance:
            print(f"DIFFERENCE: interval [{delta*i}, {delta*(i+1)}) has {len(buckets[i])} points, ratio {point_ratio} and length ratio {length_ratio}")
            found_problem = True
        
        #print(f"{len(points_in_the_interval)}] [{interval_a}, {interval_b}) contains point ratio: {len(points_in_the_interval) / len(points)}")
    if not found_problem:
        print("All intervals and points within tolerance!")
    return

arr = [random() for x in range(0, 100000000)]

checkers_1d(arr, .00001, (0, 1), 10000)