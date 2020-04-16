import numpy as np
from Maze import negative_maze, print_values, print_policy


# Create a minimum threshold to check for convergence
THRESHOLD = 1e-3
# A discount variable is added so that the program is not greedy
GAMMA = 0.9
ALL_ACTIONS = ('U', 'D', 'L', 'R')

if __name__ == '__main__':

    # Make a grid object
    grid = negative_maze()
    print("Rewards: ")
    print_values(grid.rewards, grid)

    # Randomly initialize a policy for all playable states
    policy = {}
    states = grid.all_states()
    for s in states:
        if s in grid.actions.keys():
            policy[s] = np.random.choice(ALL_ACTIONS)
    print("Random initial Policy")
    print_policy(policy, grid)

    # Randomly initialize a Value for all playable states and 0 for other states
    V = {}
    for s in states:
        if s in grid.actions.keys():
            V[s] = np.random.random()
        else:
            V[s] = 0
    print("Initial Random Values: ")
    print_values(V, grid)

    # Policy evaluation and improvement
    while True:
        # Variable to see the biggest change between 2 consecutive values
        biggest_change = 0
        for s in states:
            # initialize old_v as the initial value in the state iteration
            old_v = V[s]

            if s in policy:
                new_v = float('-inf')

                # Go through each action to find the best one with the highest value
                for a in ALL_ACTIONS:

                    # "Play" the game and get rewards
                    grid.set_state(s)
                    r = grid.move(a)

                    # Calculate the Value using the bellman equation
                    v = r + GAMMA*V[grid.current_state()]

                    # Check for max / best value corresponding to an action
                    if v > new_v:
                        new_v = v
                        best_a = a

                # Update the Value and the Policy from the above calculation
                V[s] = new_v
                policy[s] = best_a

                # Check for convergence and break if converged
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))

        if biggest_change < THRESHOLD:
            break

    # Print the necessary details
    print("New Policy ")
    print_policy(policy, grid)

    print("New Values: ")
    print_values(V, grid)