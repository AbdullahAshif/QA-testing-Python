class Env:
    def __init__(self, env):
        self._env = env

    @property
    def env(self):
        return self._env
