"""
A node module is used to define the necessary data structure and
method for a physical machine in the cluster.
"""

from .microservice import Microservice

class Node:

    name: str
    """
    The name of the machine
    """

    microservices: list[Microservice]
