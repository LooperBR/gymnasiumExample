import gymnasium as gym
import time
env = gym.make('Blackjack-v1',render_mode="human")
observation, info = env.reset()

for i in range(1000):
    action = env.action_space.sample()
    if(action ==0):
        print("Stand")
    else:
        print("HIT")    
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()
    if terminated or truncated:
        observation, info = env.reset()
    time.sleep(0.5)