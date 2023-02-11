#!/usr/bin/env python3
"""This is the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guests = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
