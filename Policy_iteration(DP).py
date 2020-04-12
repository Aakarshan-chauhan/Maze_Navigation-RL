import numpy as np
from GridWorld import standard_grid, negative_grid, print_values, print_policy

THRESHOLD = 1e-3
ALL_ACTIONS = ('U', 'D', 'L', 'R')
GAMMA = 0.9

if __name__ == '__main__':
    # Initialize a grid object
    grid = negative_grid()
    states = grid.all_states()
    # Randomly initialize the policy for all possible actions
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ALL_ACTIONS)
    print("Initial Policy: ")
    print_policy(policy, grid)

    # Randomly initialize the values for all possible actions and 0 for others
    V = {}
    for s in states:
        if s in policy:
            V[s] = np.random.random()
        else:
            V[s] = 0
    print("Initial Values: ")
    print_values(V, grid)

    # Loop till previous Policy  = updated policy
    while True:

        # Iterative Policy Evaluation
        while True:
            biggest_change = 0
            for s in states:
                old_v = V[s]
                if s in policy:
                    a = policy[s]
                    grid.set_state(s)
                    r = grid.move(a)
                    V[s] = r + GAMMA * V[grid.current_state()]
                    biggest_change = max(biggest_change, np.abs(old_v - V[s]))

            if biggest_change < THRESHOLD:
                break

        # Update Policy
        Policy_changed = False
        for s in states:
            if s in policy:
                old_a = policy[s]
                new_a = None
                best_value = float('-inf')

                # Best value will be taken as the Max over all actions in a particular state
                for a in ALL_ACTIONS:
                    grid.set_state(s)
                    r = grid.move(a)
                    v = r + GAMMA*V[grid.current_state()]
                    if v > best_value:
                        best_value = v
                        new_a = a

                # Update the policy with the action corresponding to best value
                policy[s] = new_a

                # If there was no change in action, optimal action already attained
                if old_a != new_a:
                    Policy_changed = True

        # If Policy did not change for a whole set of states, no more iterations are required
        if not Policy_changed:
            break

    # Print the required information
    print("Changed Values: ")
    print_values(V, grid)
    print("New Policy: ")
    print_policy(policy, grid)
