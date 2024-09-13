import gymnasium as gym
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
# Create an environment
env = gym.make("CartPole-v1", render_mode="rgb_array")
total_reward = 0
nr_episodes = 1000
nr_actions = env.action_space.n
for _ in tqdm(range(nr_episodes)):
    env.reset()
    terminated = False
    truncated = False
    while not (terminated or truncated):
        chosen_action = np.random.randint(nr_actions)
        s_prime, r, terminated, truncated, info = env.step(action=chosen_action)
        total_reward += r
        state_in_rgb = env.render()
        # plot the state which is a 3D array with rgb values
        plt.imshow(state_in_rgb)
        # wait for 0.1 seconds
        plt.pause(0.1)
print(total_reward / nr_episodes)
""" import gymnasium as gym
# Create an environment
env = gym.make("CartPole-v1", render_mode="rgb_array")

# 0 - Reset the environment
env.reset()
# 1 - Let's examine the env

# 1.1 - Check the observation space of the agent
env.observation_space
# 1.2 - Check the action space of the agent
env.action_space
# 1.3 - Render the env
# 1.4 - Reset the environment
env.step(action=1)
env.render()
# 1.5 - Check the source code of the env.

# 2 - Interact with environment
# 2.1 - Push the cart to the left once
# 2.2 - Repeat the action above until the pole falls, i.e. the episode is terminated
print("end of the script") """
