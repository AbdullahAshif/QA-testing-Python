class EnvData:
    def __init__(self, protocol, domain, wait, host):
        self._protocol = protocol
        self._domain = domain
        self._wait = wait
        self._host = host

    @property
    def protocol(self):
        return self._protocol

    @property
    def domain(self):
        return self._domain

    @property
    def wait(self):
        return self._wait

    @property
    def host(self):
        return self._host

    def get_host(self):
        return self._protocol + "://" + self._domain
