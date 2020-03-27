import numpy as np
import matplotlib.pyplot as plt
from GridWorld import standard_grid, negative_grid
from iterative_policy_evalutaion import print_values, print_policy

THRES = 1e-3
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

if __name__ == '__main__':

    # Each step in this grid has a negative reward
    # so that shorter path is encouraged
    grid = negative_grid()
    #grid = standard_grid()
    print("rewards:")
    print_values(grid.rewards, grid)

    # Randomly initialize a policy and update as we learn
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ALL_POSSIBLE_ACTIONS)

    # Initial policy
    print("Initial Policy")
    print_policy(policy, grid)

    # Initialize V(s)
    V = {}
    states = grid.all_states()
    for s in states:
        # Non terminal state
        if s in grid.actions:
            V[s] = np.random.random()
        else:
            # Terminal State
            V[s] = 0

    # Loop till policy keeps changing.
    while True:

        # Iterative Policy Evaluations
        while True:
            biggest_change = 0
            for s in states:
                old_v = V[s]

                if s in policy:
                    a = policy[s]
                    grid.set_state(s)
                    r = grid.move(a)
                    V[s] = r + GAMMA*V[grid.current_state()]
                    biggest_change = max(biggest_change, np.abs(V[s]- old_v))

            if biggest_change < THRES:
                break

        # Update Policy
        policy_changed = True
        for s in states:
            if s in policy:
                old_a = policy[s]
                new_a = None
                best_value = float('-inf')

                for a in ALL_POSSIBLE_ACTIONS:
                    grid.set_state(s)
                    r = grid.move(a)
                    v = r + GAMMA*V[grid.current_state()]

                    if v > best_value:
                        new_a = a
                        best_value = v
                policy[s] = new_a

                if new_a != old_a:
                    policy_changed = False
        if policy_changed:
            break
    print("Values:")
    print_values(V, grid)
    print("Policy:")
    print_policy(policy, grid)