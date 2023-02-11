#!/usr/bin/env python3
"""A class for Review"""

from model.base_model import BaseModel


class Review(BaseModel):
    """
    A Review Class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
