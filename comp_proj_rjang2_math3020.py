import numpy as np

def virus_montecarlo(n, p, r):
    sample_sum = 0
    all_infected_sum = 0
    once_infected_sum = 0
    trials = 10000
    for i in range(trials):
        sample = virus_sample(n, p, r)
        sample_sum = sample_sum + sample[0]
        all_infected_sum = all_infected_sum + sample[1]
        once_infected_sum = once_infected_sum + sample[2]

    print("Expected time it takes to remove the virus:" + 
        str(float(sample_sum)/trials))
    print("Probability that each computer gets infected at least once:" + 
        str(float(all_infected_sum)/trials))
    print("Expected number of computers that get infected:" + 
        str(float(once_infected_sum)/trials))
    return 

def virus_sample(n, p, r):
    n_infected = 1
    days = 0
    once_infected = 1
    all_infected = 0

    if (n < 1):
        return (0, 0, 0)
    if (n == 1):
        return (1, 1, 1)

    comp = np.zeros(n, dtype=int)
    comp[0] = 1
    infected_once = np.zeros(n, dtype=int)
    infected_once[0] = 1

    while (n_infected > 0):
        for i in range(n):
            for j in range(n):
                if (comp[i] == 1 and comp[j] == 0):
                    seed = np.random.rand()
                    if (seed < p):
                        comp[j] = 2

        for i in range(n):
            if (comp[i] == 2):
                comp[i] = 1  
                infected_once[i] = 1

        fix_count = 5
        for i in range(n):
            if (comp[i] == 1 and fix_count > 0):
                comp[i] = 0
                fix_count = fix_count - 1

        n_infected = np.count_nonzero(comp)
        days = days + 1

    once_infected = np.count_nonzero(infected_once)
    if (np.count_nonzero(infected_once) == n):
        all_infected = 1
    
    return (days, all_infected, once_infected)

print(virus_montecarlo(20, 0.1, 5))