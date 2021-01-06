import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# # ----------- GridWorld ----------- # #

register(
    'GridNavi-v2',
    entry_point='toy_navigation_envs.envs.gridworld:GridNavi',
    kwargs={'num_cells': 5, 'num_steps': 15, 'n_tasks': 2,
            'is_sparse': False, 'return_belief_rewards': True,
            'seed': None},
    # kwargs={'num_cells': 5, 'num_steps': 30, 'n_tasks': 2},
)

# # ----------- Point Robot ----------- # #
register(
    'PointRobot-v0',
    entry_point='toy_navigation_envs.envs.point_robot:PointEnv',
    kwargs={'max_episode_steps': 60, 'n_tasks': 1},
)


register(
    'PointRobotSparse-v0',
    entry_point='toy_navigation_envs.envs.point_robot:SparsePointEnv',
    kwargs={'max_episode_steps': 60, 'n_tasks': 1, 'goal_radius': 0.2},
)