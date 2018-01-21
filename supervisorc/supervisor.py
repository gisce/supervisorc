"""Supervisor module
"""
from __future__ import absolute_import
import xmlrpclib

from .process import Process


class Supervisor(object):
    """Supervisor instance
    """
    def __init__(self, url):
        """
        :param url: Url to connect to supervisor XML-RPC API.
        """
        self.server = xmlrpclib.Server(url)
        self.supervisor = self.server.supervisor

    @property
    def version(self):
        """Server version's.
        """
        return self.supervisor.getSupervisorVersion()

    @property
    def identification(self):
        """Server identification.
        """
        return self.supervisor.getIdentification()

    @property
    def processes(self):
        """a `list` of configured processes.
        """
        for proc in self.supervisor.getAllProcessInfo():
            yield Process(self.server, proc['name'])

    def reload(self):
        """Reloads the configuration
        """
        return self.supervisor.reloadConfig()
