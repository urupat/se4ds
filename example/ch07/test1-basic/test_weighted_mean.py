from ch07_functions1 import weighted_mean # ❶

def test_weighted_mean(): # ❷

    list_a = [1, 2, 4]
    list_b = [1, 2, 4] # ❸

    result = weighted_mean(list_a, list_b) # ❹

    assert result == 3 # ❺

