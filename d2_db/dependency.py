from typing import Type

from d2_db.services import ColorService
from d2_db.services.__base__ import BaseService


def create_dependency() -> list[Type[BaseService]]:
    """
    The data txt files depend on one another. This file creates a dependency graph and outputs the sequence of objects
    to insert.
    """
    # TODO implement this
    return [
        ColorService
    ]
