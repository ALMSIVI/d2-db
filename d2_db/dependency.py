from typing import Type

from services import *
from services.__base__ import BaseService


def create_dependency() -> list[Type[BaseService]]:
    """
    The data txt files depend on one another. This file creates a dependency graph and outputs the sequence of objects
    to insert.
    """
    # TODO implement this
    return [
        BodyLocService,
        ColorService,
        CompositService,
        EventService,
        PlayerClassService,
        StorePageService,
    ]
