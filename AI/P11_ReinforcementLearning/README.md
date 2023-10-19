# P11_ReinforcementLearning

## Resources

- <https://ojs.aaai.org/index.php/AAAI/article/view/18841>
- <https://www.youtube.com/watch?v=Dw3BZ6O_8LY>
- <https://en.wikipedia.org/wiki/Reinforcement_learning>
- <https://pytorch.org/tutorials/intermediate/mario_rl_tutorial.html>

Reinforcement Learning is an area of machine learning concerned with how intelligent agents ought to take actions in an environment in order to maximize the notion of cumulative reward.

The environment is typically stated in the form of a Markov Decision Problem (MDP), because many reinforcement learning algorithms for this context utilize dynamic programming techniques.

A basic RL is modelled as a Markov Decision Process (MDP) which is a 5-tuple (S, A, P, R, γ) where:

- S is a finite set of states
- A is a finite set of actions
- $P_a(s, s') = P_r(s_{t+1} | s_t = s, a_t = a)$ is a state transition probability matrix
- R is a reward function
- γ is a discount factor (not used here...)

A basic RL agent AI interacts with its environment in discrete time steps. At each time t, the agent receives the current state $s_t$ and reward $r_t$. It then chooses an action $a_t$ from the set of actions $A(s_t)$ from the set of available actions, which is subsequently sent to the environment. The environment moves to a new state $s_{t+1}$ and the reward $r_{t+1}$ associated with the transition $(s_t, a_t, s_{t+1})$ is determined. The goal of a RL agent is to learn a policy.

$$ \pi : A \times S \rightarrow [0, 1], \pi(a, s) = P_r(a_t = a | s_t = s) $$

that maximizes the expected cumulative reward.

The set of actions can further be restricted by the environment regardless of the observability of the RL agent's Markov Decision Problem.

---

This case study is based on a simplified version of the 1983 Mario Bros. side-scroller by Nintendo Co.

On every time step the Mario agent must select an action in a 3 dimensional action space. Dimension 1 : {-1, 0, 1} corresponding to moving left, stopping, and moving right. Dimension 2 : {0, 1} corresponds to not jumping and jumping and Dimension 3 : {0, 1} corresponds to running and walking.

The agent receives state information as a 21 x 16 array of tiles representing the state space corresponding to a view of the game world. Each tile contains information about weather Mario can travel through the tile, if Mario can walk on top of the tile etc.

The agent's goal is to learn a policy that can receive large amounts of rewards. A action-value function Q was the target for this RL agent. It accurately predicts the long term reward for an action in a given state. Mario receives a small negative reward for every time-step, a negative reward for dying, a positive reward for collecting coins or power-ups and a large +ve reward for finishing the level.

A class `Mario` was created to represent the agent in the game.

Mario should be able to "Act", "Remember", and "Learn".

---

For any given state, an agent can choose to do the most optimal action (exploit) or a random action (explore)

Mario randomly explores with a chance of self.exploration_rate; when he chooses to exploit, he relies on a neural network to provide the most optimal action.

The remember action is split into 2, `cache()` and `recall()`

`cache()` : every time Mario performs an action, it stores the reward obtained to its memory.

`recall()`: Mario randomly samples a batch of experiences from his memory and uses that to learn the game.

The learning is handled by a DDQN (Double Deep Q Network) [Relating to the Q function].
DDQN uses 2 networks $\theta_{online}$ and $\theta_{target}$ that independely approximate the optimal action-value function.

As mario samples inputs from his reply buffer, we compute the losses and back propogate the losses down $\theta_{online}$ to update its parameters. $\theta_{target}$ doesn't update through back propogation. Instead we periodically copy $\theta_{online}$ to $\theta_{target}$

The training reaches an acceptable loss around the 40 plays mark, but to make sure it can complete any level, a larger 40,000 plays training set must be used.

---
