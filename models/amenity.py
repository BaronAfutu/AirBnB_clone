#!/usr/bin/python3
"""Define the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity.

    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
