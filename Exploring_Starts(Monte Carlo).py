from Maze import negative_maze, standard_maze, print_policy, print_values
import numpy as np

ALL_ACTIONS = ('U', 'D', 'L', 'R')
GAMMA = 1


def play_game(p, Grid):
    # Randomly choose a starting position from all valid states
    start_idx = np.random.choice(len(list(Grid.actions.keys())))
    Grid.set_state(list(Grid.actions)[start_idx])

    # Let the first action be uniformly random
    state = Grid.current_state()
    action = np.random.choice(ALL_ACTIONS)

    # Create a triple of state, action and reward
    # It can be understood as doing action a at state s will give a reward 0
    sar = [(state, action, 0)]

    # A set to keep track of visited states
    seen_states = set()
    seen_states.add(state)

    # Number of steps
    n = 0
    while True:

        # Get the rewards by moving on the grid
        r = Grid.move(action)
        n += 1
        state = Grid.current_state()

        if state in seen_states:
            r = -10. / n
            # No action to be done if same state is visited twice hence return None
            sar.append((state, None, r))
            break

        elif Grid.game_over():
            # No action to be done after reaching terminal states hence return None
            sar.append((state, None, r))
            break

        else:
            action = policy[state]
            sar.append((state, action, r))
        seen_states.add(state)

    # Returns and State Action Returns list
    G = 0
    saG = []

    first = True
    for s, a, r in reversed(sar):
        # Ignore the first value since in reversed it will be a terminal state
        if first:
            first = False
        else:
            saG.append((s, a, G))

        # Calculate the Returns from the modified bells equation
        G = r + GAMMA * G

    saG.reverse()
    return saG


# Function to return the argmax value from a given dictionary and its key
def max_dict(d):
    max_key, max_val = None, float('-inf')
    for k, v in d.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key, max_val


if __name__ == '__main__':
    grid = negative_maze()

    # Randomly initialize a policy
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ALL_ACTIONS)

    # Q = mean of returns G for state s and action a
    Q = {}
    G = {}
    state = grid.all_states()
    for s in state:
        if s in grid.actions.keys():
            Q[s] = {}
            for a in ALL_ACTIONS:
                Q[s][a] = 0
                G[(s, a)] = []

    biggest_changes = []
    # Play game and get returns
    for t in range(20000):
        if t % 100 == 0:
            print("Episode %d" % t)
        seen_state_actions = set()
        biggest_change = 0
        saG = play_game(policy, grid)
        for s, a, g in saG:
            sa = (s, a)
            # Check if same action not done in same state twice.
            if sa not in seen_state_actions:
                old_q = Q[s][a]
                G[sa].append(g)
                Q[s][a] = np.mean(G[sa])
                biggest_change = max(biggest_change, np.abs(old_q - Q[s][a]))
                seen_state_actions.add(sa)
        biggest_changes.append(biggest_change)

        # Put optimal policy as the action with the max return on a particular state
        for s in policy.keys():
            policy[s] = max_dict(Q[s])[0]

    print_policy(policy, grid)

    V = {}
    for s, a in Q.items():
        V[s] = max_dict(Q[s])[1]

    print_values(V, grid)
