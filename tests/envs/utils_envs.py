import gymnasium


class RegisterDuringMakeEnv(gymnasium.Env):
    """Used in `test_registration.py` to check if `env.make` can import and register an env"""

    def __init__(self):
        self.action_space = gymnasium.spaces.Discrete(1)
        self.observation_space = gymnasium.spaces.Discrete(1)


class ArgumentEnv(gymnasium.Env):
    observation_space = gymnasium.spaces.Box(low=-1, high=1, shape=(1,))
    action_space = gymnasium.spaces.Box(low=-1, high=1, shape=(1,))

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3


# Environments to test render_mode
class NoHuman(gymnasium.Env):
    """Environment that does not have human-rendering."""

    metadata = {"render_modes": ["rgb_array_list"], "render_fps": 4}

    def __init__(self, render_mode=None):
        assert render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode


class NoHumanOldAPI(gymnasium.Env):
    """Environment that does not have human-rendering."""

    metadata = {"render_modes": ["rgb_array_list"], "render_fps": 4}

    def __init__(self):
        pass


class NoHumanNoRGB(gymnasium.Env):
    """Environment that has neither human- nor rgb-rendering"""

    metadata = {"render_modes": ["ascii"], "render_fps": 4}

    def __init__(self, render_mode=None):
        assert render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
