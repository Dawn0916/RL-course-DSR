"""Your first learning agent: template."""
# 0 - Choose an algorithm from ray.rllib.algorithms, e.g. ray.rllib.algorithms.xxx as
# xxxConfig
from ray.rllib.algorithms.dqn.dqn import DQNConfig
config =DQNConfig()

config.environment(env = "CartPole-v1").framework(
    framework = "tf2", eager_tracing = True
).rollouts(num_rollout_workers = 4, num_envs_per_worker =2).evaluation(
    evaluation_config = {"explore": False},
    evaluation_duration = 10,
    evaluation_interval = 1,
    evaluation_duration_unit = "episodes",
)

print("hi")
# 1 -  Build an agent
# 1.1 - Get the default config of xxxConfig()
# 1.2 - Examine the config by converting it to a dict via .to_dict() method
# 1.3 - Modify the config if needed, e.g. change the "num_gpus" to 0,
# 1.4 - Introduce the environment to the agent's config
# 1.5 - Build the agent
# 2 - Train the agent for one training round and get the reports
# 3 - Run a loop for nr_trainings = 50 times

# 4 - Visualize the trained agent; This is similar to running the random_agent,
# except that this time we have a trained agent
# 4.1 - Create an environment similar to the training env.
# 4.2. Let the agent choose an action;
# 4.3. and pass it to the environment
# 4.4. How much reward did you get for that action? Keep the score!
# 4.5. Repeat the 4.{2,3, 4} until the end of the episode
# 4.6. How much total reward you got? What does it mean to have large/small reward?
print("Good-bye.")
