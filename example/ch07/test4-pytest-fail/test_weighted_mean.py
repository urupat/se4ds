from ch07_functions1 import weighted_mean

def test_weighted_mean():

    list_a = [1, 2, 4]
    list_b = [1, 2, 5]

    result = weighted_mean(list_a, list_b)

    assert result == 3

