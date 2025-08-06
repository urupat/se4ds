import logging

logging.basicConfig(filename="ch05_logs.log",
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s %(message)s')

def weighted_mean(num_list, weights):
    running_total = 0
    for i in range(len(num_list)):
        running_total += num_list[i] * weights[0]
        logging.debug(f"The running total at step {i} is {running_total}")
    return running_total/sum(weights)

print(weighted_mean([1, 6, 8], [1, 3, 2]))
