import rlcard
from rlcard.utils import (
    get_device,
    set_seed,
)
from examples.utils import (
    print_trajectories
)
import torch

num_players = 5
model_path = 'experiments/no_limit_holdem_dqn_result/model.pth'

# Check whether gpu is available
device = get_device()

# Make the environment with seed
env = rlcard.make('no-limit-holdem', config={'game_num_players': num_players})

players = []
for _ in range(num_players):
    agent = torch.load(model_path, map_location=device)
    agent.set_device(device)
    players.append(agent)
env.set_agents(players)

trajectories, payoffs, trajectories_humanization = env.run(is_training=False)

print_trajectories(trajectories_humanization, payoffs)
