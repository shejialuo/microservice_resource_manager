"""
This module defines
"""

class MicroserviceInstance:
    """
    A `MicroserviceInstance` is a running instance of a microservice.

    """

    name: str
    """
    The instance name should be the format `nodename.microservice.instanceID`
    """

    current_memory_usage: int


class Microservice:

    name: str
    """
    The name of the microservice
    """

    cpu: int
    """
    The number of CPU cores the microservice requires
    """