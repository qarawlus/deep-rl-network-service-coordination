from rlsp.utils.experiment_result import ExperimentResult
MAX_EPISODE_STEPS = 200


class AgentHelper(object):
    """Data class to hold agent params"""
    def __init__(self, agent_config, network, service, sim_config, seed, steps, weights, verbose,
                 DATETIME, test, append_test, test_episodes, sim_seed, gen_scenario):
        self.max_episode_steps = MAX_EPISODE_STEPS
        self.verbose = verbose
        self.agent_config_path = agent_config
        self.network_path = network
        self.service_path = service
        self.sim_config_path = sim_config
        self.seed = seed
        self.experiment_id = f"{DATETIME}_seed{seed}"
        self.result = ExperimentResult(self.experiment_id)
        self.weights = weights
        self.steps = steps
        self.agent = None
        self.result_base_path = None
        self.graph_base_path = None
        self.result_file = None
        self.config = None
        self.config_dir = None
        self.logfile = None
        self.weights_path = None
        self.graph_path = None
        self.env = None
        self.test = test
        self.train = True
        self.test_mode = test
        if self.test:
            self.train = False
        self.append_test = append_test
        if self.append_test:
            self.test = self.experiment_id
        self.gen_scenario = gen_scenario
        self.gen_scenario_test = False
        self.gen_scenario_result_base_path = None
        self.callbacks = None
        self.test_episodes = test_episodes
        self.sim_seed = sim_seed
