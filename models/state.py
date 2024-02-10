#!/usr/bin/python3
"""Define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): Name of the state.
    """

    name = ""
