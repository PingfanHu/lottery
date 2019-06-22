import random
N_trials = 100000
N_elements = 4
N_types = 4
N_picks = 5
success = 0

for n in range(0, N_trials):
    listA = [1, 2, 3, 4]*N_elements
    # listA = sorted(listA)
    # listA = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
    listB = []

    for x in range(0, N_picks):
        listB.append(listA.pop(random.randint(0, len(listA) - 1 - x)))

    listB = list(set(listB))
    if len(listB) == N_types:
        success = success + 1


print('rate equals', success/N_trials*100, '%')