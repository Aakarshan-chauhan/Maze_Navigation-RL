# Define a class for the maze board
class Maze:

    # Initialize number of rows, cols and start position
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]
        self.start = start

    def set(self, rewards, actions):
        self.rewards = rewards
        self.actions = actions

    def set_state(self, state):
        self.i = state[0]
        self.j = state[1]

    def current_state(self):
        return (self.i, self.j)

    def is_terminal(self, state):
        return state not in self.actions

    def move(self, action):

        if action in self.actions[(self.i, self.j)]:
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'L':
                self.j -= 1
            elif action == 'R':
                self.j += 1

        return self.rewards.get((self.i, self.j), 0)

    def undo_move(self, action):

        if action == 'U':
            self.i += 1
        elif action == 'D':
            self.i -= 1
        elif action == 'L':
            self.j += 1
        elif action == 'R':
            self.j -= 1

    def game_over(self):
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())


def standard_maze(rows=8, cols=10, start=(7, 0)):
    g = Maze(rows, cols, start)
    stoppers = []
    stoppers = [[(7, 7)], [(7, 3)], [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (6, 1), (7, 1), (1, 2),
        (6, 2), (1, 3), (3, 3), (4, 3), (5, 3), (6, 3), (0, 5), (1, 5), (7, 5),
        (7, 6), (5, 6), (5, 7), (0, 8), (2, 8), (4, 8), (5, 8), (7, 8), (0, 9), (7, 9),
        (7, 2)
    ]]
    '''
    temp = []
    ar, b = input("Enter a win: ").split(',')
    stoppers.append(([[int(ar), int(b)]]))

    ar, b = input("Enter a loss: ").split(',')
    stoppers.append(([[int(ar), int(b)]]))

    for t in range(int(input("Enter number of rocks"))):
        ar, b = input("Enter a rock: ").split(',')
        temp.append(([int(ar), int(b)]))
    stoppers.append(temp)
    actions = {}'''

    actions = {}
    for i in range(rows):
        for j in range(cols):
            list1 = []
            if [(i, j)] not in stoppers and (i, j) not in stoppers[-1]:

                if (i + 1, j) not in stoppers[-1] and i + 1 < rows:
                    list1.append('D')
                if (i - 1, j) not in stoppers[-1] and i - 1 >= 0:
                    list1.append('U')
                if (i, j + 1) not in stoppers[-1] and j + 1 < cols:
                    list1.append('R')
                if (i, j - 1) not in stoppers[-1] and j - 1 >= 0:
                    list1.append('L')

            actions[i, j] = tuple(list1)
    '''
    for i in range(rows):
        for j in range(cols):
            list1 = []
            if [[i, j]] not in stoppers and [i, j] not in stoppers[-1]:

                if [i + 1, j] not in stoppers[-1] and i + 1 < rows:
                    list1.append('D')
                if [i - 1, j] not in stoppers[-1] and i - 1 >= 0:
                    list1.append('U')
                if [i, j + 1] not in stoppers[-1] and j + 1 < cols:
                    list1.append('R')
                if [i, j - 1] not in stoppers[-1] and j - 1 >= 0:
                    list1.append('L')

            actions[i, j] = tuple(list1)
            '''
    rewards = {}
    for win in stoppers[0]:
        rewards[tuple(win)] = 1

    for loss in stoppers[1]:
        rewards[tuple(loss)] = -5

    actions = {k: v for k, v in actions.items() if v is not ()}
    g.set(rewards, actions)
    return g


def negative_maze(step_cost=-0.1, rows=8, cols=10, start=(7, 0)):
    g = standard_maze(rows, cols, start)
    for i in list(g.actions.keys()):
        g.rewards[i] = step_cost
    return g


def print_values(Val, g):
    for i in range(g.rows):
        print("----------------------------------------------------------------------")
        for j in range(g.cols):
            v = Val.get((i, j), 0)
            if v > 0:
                print(" %.2f|" % v, end="")
            elif v == 0:
                print(" ### |", end="")
            else:
                print("%.2f|" % v, end="")
        print("")


def print_policy(P, g):
    for i in range(g.rows):
        print("----------------------------------------------------------------------")
        for j in range(g.cols):
            p = P.get((i, j), " ")
            if p != '':
                print("%s      |" % p, end="")
            else:
                print(" ### |", end="")
        print("")
