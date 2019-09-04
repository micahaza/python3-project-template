from myapp.distance_calculator import get_distances


def test_with_two_points():
    params = [(3, 3), (4, 4)]
    print(get_distances(params))
    assert get_distances(params) == ([(3, 3), (4, 4)], [(3, 3), (4, 4)])
    params = [(3, 3), (4, 4), (10, 10)]
    # print(get_distances(params))
    assert get_distances(params) == ([(3, 3), (4, 4)], [(3, 3), (10, 10)])
