from GridWorld import standard_grid, negative_grid, print_policy, print_values

if __name__ == '__main__':
    grid = standard_grid()

    # states is are the positions
    states = grid.all_states()

    # initialize V(s) = 0
    V = {}
    for s in states:
        V[s] = 0

    # gamma = discount factor. 1 = all future rewards are equal,
    # 0 = greedy
    gamma = 1

    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]
            # Check for terminal states otherwise
            # V(s) has no value
            if s in grid.actions:

                new_v = 0
                # policy of action given state. Let each action
                # have equal probability
                p_a = 1.0 / len(grid.actions[s])
                for a in grid.actions[s]:
                    # set_state sets the coordinates of the agent.
                    grid.set_state(s)

                    # move(a) changes the coordinates according to the action a
                    # and hence creates a new state.
                    # Returns the reward at the new state.
                    r = grid.move(a)

                    # Bellman's Equation for deterministic moves.
                    # Since the moves are not random, i.e. if i want to go right,
                    # i will go right 100 percent of the time
                    # hence  the p(s',r | s, a) = 1
                    # grid.current_state returns state. State = s' since we used move(a) to change it
                    new_v += p_a * (r + gamma * V[grid.current_state()])

                V[s] = new_v

                # Calculate the maximum change in Value function between two states
                biggest_change = max(biggest_change, np.abs(V[s] - old_v))

        # If biggest change in V(s) in state s is very low, exit. (convergence)
        if biggest_change < THRESH:
            break
    print("Values for Uniformly random actions:")
    print_values(V, grid)
    print("\n\n")
# Policy Evaluation can help us understand the impact of an action on the Value of the state
# and improve it later
