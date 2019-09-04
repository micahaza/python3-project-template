
import math

notGoodPointListException

def distance(first, second):
    return math.sqrt(((first[0] - second[0]) * (first[0] - second[0])) + ((first[1] - second[1]) * (first[1] - second[1])))

def get_distances(points):

    closest_pair = None
    closest_distance = None
    farest_pair = None
    farest_distance = None
    i = j = 0

    while i < len(points):
        while j < len(points[i + 1:]):
            first = points[i]
            second = points[j]
            current_dist = distance(first, second)
            if closest_distance is None or closest_distance > current_dist:
                closest_distance = current_dist
                closest_pair = [points[i], points[j]]
            if farest_distance is None or farest_distance < current_dist:
                farest_distance = current_dist
                farest_pair = [points[i], points[j]]
            j += 1
        i += 1
    return closest_pair, farest_pair
