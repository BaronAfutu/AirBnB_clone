#!/usr/bin/python3
"""Define the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Review text.
    """

    place_id = ""
    user_id = ""
    text = ""
