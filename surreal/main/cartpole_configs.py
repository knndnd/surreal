cartpole_learn_config = {
    'model': {
        'convs': [],
        'fc_hidden_sizes': [64],
        'dueling': False
    },
    'algo': {
        'lr': 1e-3,
        # 'train_freq': 1,
        'optimizer': 'Adam',
        'grad_norm_clipping': 10,
        'gamma': .99,
        'target_network_update_freq': 250 * 64,
        'double_q': True,
        'exploration': {
            'schedule': 'linear',
            'steps': 30000,
            'final_eps': 0.01,
        },
        'prioritized': {
            'enabled': False,
            'alpha': 0.6,
            'beta0': 0.4,
            'beta_anneal_iters': None,
            'eps': 1e-6
        },
    },
}

cartpole_env_config = {
    'action_spec': {
        'dim': [2],
        'type': 'discrete'
    },
    'obs_spec': {
        'dim': [4],
    }
}