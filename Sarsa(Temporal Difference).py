import matplotlib.pyplot as plt
import numpy as np

from Maze import negative_maze, print_values, print_policy

ALL_ACTIONS = ('U', 'D', 'L', 'R')
GAMMA = 0.9
ALPHA = 1.0


# Epsilon Soft for exploration
def random_action(a, e=0.1):
    prob = np.random.random()

    if prob > (1 - e + e / len(ALL_ACTIONS)):
        return a
    else:
        return np.random.choice(ALL_ACTIONS)


# Argmax key from a dictionary
def max_dict(d):
    max_k, max_v = None, float('-inf')
    for k, v in d.items():
        if v > max_v:
            max_k = k
            max_v = v
    return max_k, max_v


if __name__ == '__main__':

    maze = negative_maze()
    print("Values: ")
    print_values(maze.rewards, maze)

    states = maze.all_states()

    # Initialize Q for all states and actions
    Q = {}
    for s in states:
        Q[s] = {}
        for a in ALL_ACTIONS:
            Q[s][a] = 0

    # This would determine the decay in learning rate after each update
    state_lr_decay = {}
    for s in states:
        state_lr_decay[s] = {}
        for a in ALL_ACTIONS:
            state_lr_decay[s][a] = 1.0

    # t signifies the decay in epsilon over time
    t = 1.0
    deltas = []

    for it in range(10000):
        if it % 100 == 0:
            t += 1e-2
        print("Episode: %d" % it)

        # Set the agent at the start position
        s = maze.start
        maze.set_state(s)

        # Choose an action using epsilon soft
        a = max_dict(Q[s])[0]
        a = random_action(a, 0.5 / t)
        biggest_change = 0

        # Play till terminal state is achieved
        while not maze.game_over():
            # Get rewards, s' and a'
            r = maze.move(a)
            s2 = maze.current_state()
            a2 = max_dict(Q[s2])[0]
            a2 = random_action(a2, 0.5/t)

            old_q = Q[s][a]

            # Update the learning rate
            lr = ALPHA / state_lr_decay[s][a]
            state_lr_decay[s][a] += 0.005

            # Calculate Q
            Q[s][a] = Q[s][a] + lr * (r + GAMMA * Q[s2][a2] - Q[s][a])
            biggest_change = max(biggest_change, np.abs(old_q - Q[s][a]))

            s = s2
            a = a2

        # Append the biggest changes to check for convergence
        deltas.append(biggest_change)

    plt.plot(deltas)
    plt.show()

    V = {}
    policy = {}
    for s in maze.actions.keys():
        a, max_q = max_dict(Q[s])
        policy[s] = a
        V[s] = max_q
    print("Policy:")
    print_policy(policy, maze)
    print("Final rewards: ")
    print_values(V, maze)
