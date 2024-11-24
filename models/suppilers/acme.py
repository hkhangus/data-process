import re
from typing import Dict, Any
from models.hotel import Hotel, Location, Amenities, Images
from models.suppilers.base import BaseSupplier

class AcmeSupplier(BaseSupplier):
    @property
    def url(self) -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
    @property
    def name(self) -> str:
        return "acme"
    
    def parse(self, hotel: Dict[str, Any]) -> Hotel:
        location = Location(
            lat=self.get_field(hotel, "Latitude", "float"),
            lng=self.get_field(hotel, "Longitude", "float"),
            address=self.get_field(hotel, "Address", "str"),
            city=self.get_field(hotel, "City", "str"),
            country=self.get_field(hotel, "Country", "str")
        )
        amenities = Amenities(
            general=[
                self.split_camel_case(" ".join(word for word in amenity.strip().split()))
                for amenity in self.get_field(hotel, "Facilities", "list")
            ],
            room=[]
        )
        images = Images(
            rooms=[],
            site=[],
            amenities=[]
        )
        return Hotel(
            id=self.get_field(hotel, "Id", "str"),
            destination_id=self.get_field(hotel, "DestinationId", "int"),
            name=self.get_field(hotel, "Name", "str"),
            location=location,
            description=self.get_field(hotel, "Description", "str"),
            amenities=amenities,
            images=images,
            booking_conditions=[]
        )
