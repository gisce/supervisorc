"""Process module
"""
class Process(object):
    """Supervisor process.
    """

    def __init__(self, server, name):
        self.server = server
        self.supervisor = self.server.supervisor
        self._name = name
        self.update_info()

    def update_info(self):
        """Internal method to update process information.
        """
        self.info = self.supervisor.getProcessInfo(self._name)

    def start(self, wait=True):
        """Start a this process.
        """
        return self.supervisor.startProcess(self._name, wait)

    def stop(self, wait=True):
        """Stop this process.
        """
        return self.supervisor.stopProcess(self._name, wait)

    def send_signal(self, signal):
        """Send a signal to the process.
        """
        return self.supervisor.signalProcess(self._name, signal)

    def send_stdin(self, stdin):
        """Send standard input to the process.
        """
        return self.supervisor.sendProcessStdin(self._name, stdin)

    def restart(self):
        """Restart this process.
        """
        self.stop()
        self.start()

    @property
    def info(self):
        """Info of the process.

        Automatically information is updated by `self.update_info()`
        """
        self.update_info()
        return self.info

    @property
    def name(self):
        """The name of the process.
        """
        self.update_info()
        return self.info['name']

    @property
    def group(self):
        """The group of the process if it is part of a group.
        """
        self.update_info()
        return self.info['group']

    @property
    def description(self):
        """The description of the process.
        """
        self.update_info()
        return self.info['description']

    @property
    def started(self):
        self.update_info()
        return self.info['start']

    @property
    def stopped(self):
        self.update_info()
        return self.info['stop']

    @property
    def now(self):
        self.update_info()
        return self.info['now']

    @property
    def state(self):
        """The state of the process (code).
        """
        self.update_info()
        return self.info['state']

    @property
    def statename(self):
        """The state of the process (name).
        """
        self.update_info()
        return self.info['statename']

    @property
    def logfile(self):
        """The logfile of the process.
        """
        self.update_info()
        return self.info['logfile']

    @property
    def stdout_logfile(self):
        """The log file of stdout.
        """
        self.update_info()
        return self.info['stdout_logfile']

    @property
    def stderr_logfile(self):
        """The logfile of stderr.
        """
        self.update_info()
        return self.info['stderr_logfile']

    @property
    def spawnerr(self):
        self.update_info()
        return self.info['spawnerr']

    @property
    def exitstatus(self):
        """Status of the exit.
        """
        self.update_info()
        return self.info['exitstatus']

    @property
    def pid(self):
        """The process identifier (pid).
        """
        self.update_info()
        return self.info['pid']
