Supervisor client
=================

This is a high level library to access to XML-RPC API of a Supervisor
instance.

.. code-block:: python

    from supervisorc import Supervisor

    supervisor = Supervisor('http://localhost:9001/RPC2')
    supervisor.version
    >>> '3.3.3'

    for process in supervisor.processes:
        print process.pid, process.name, process.statename

