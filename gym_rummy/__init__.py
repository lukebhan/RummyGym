from gym.envs.registration import register

register(
        id='Rummy-v0',
        entry_point='gym_rummy.envs:RummyEnv')
