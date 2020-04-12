The following contents are potential solutions for solving a grid (or a maze) by using Reinforcement Learning.

***Problem**: The game consists of a grid( default: 3 x 4) which has one cell where the agent will win and one cell where it will loose.
There can be multiple walls set in the grid which the agent would avoid. The goal of the agent is to start at a position and reach the win cell.


**The grid can be of two types:**

  1. Standard grid: A normal grid. Doesnt promote shortest path to the win.
  
  2. Negative grid: Each cell has a -0.1 reward which helps the agent to prioritize the shortest path.

The agent would show its path for each cell using the letters *U, D, L or R* to specify the direction it would go in.

  
We are going to use *Bellman's Equations* to solve this grid.
```
V[s] = r + Gamma * V[s']
```
`r` is the sum of rewards associated directly with that particular state.
Where `V[s]`(Expected Value of state `s`) signifies the importance of a state(`s`) with respect to the states surrounding it. It can be thought of as a measure of its "closeness" to the desired state.

`Gamma` is called a discount factor. It can range from 0 to 1. It signifies how important future rewards are. A discount of 0 would make the agent **greedy** and focus on the immidiate reward. A discount of 1 would rank all future rewards as equally important and make finding the shortest path harder. Hence a value around 0.8 or 0.9 is considered.

`V[s']` is the expected value of state following the state `s`. If state was dependent solely on time, `s` would be `state at time t` and `s'` would be `state at time t+1`.

**A Bellman Equations can be solved by various methods:

  1. Dynamic Programming:  
                           
                           - Policy Iteration
                           
                           - Value Iteration
  2. Monte Carlo
  
  
  3. Temporal Difference: 
  
                          - SARSA
                          
                          - Q-Learning
                          
# A Reinforcement Learning problem can be broken down into two sub parts:

  1. Prediction Problem: Calculate Values or Returns when a policy(set of actions for a particular state) is already given.

  2. Control Problem: Find the optimal policy ("best" set of actions for each state) and corresponding value function.


