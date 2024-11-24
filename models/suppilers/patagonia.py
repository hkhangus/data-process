from models.hotel import Hotel, Location, Amenities, Images, Image
from models.suppilers.base import BaseSupplier

class PatagoniaSupplier(BaseSupplier):
    @property
    def url(self) -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"
    @property
    def name(self) -> str:
        return "patagonia"
    
    def parse(self, hotel: dict) -> Hotel:
        location = Location(
            lat=self.get_field(hotel, "lat", "float"),
            lng=self.get_field(hotel, "lng", "float"),
            address=self.get_field(hotel, "address", "str"),
            city="",
            country=""
        )
        amenities = Amenities(
            general=[],
            room=[
                self.split_camel_case(" ".join(word for word in amenity.strip().split()))
                for amenity in self.get_field(hotel, "amenities", "list")
            ],
        )
        images = Images(
            rooms=[Image(link=img["url"], description=img["description"]) for img in hotel.get("images", {}).get("rooms", [])],
            site=[],
            amenities=[Image(link=img["url"], description=img["description"]) for img in hotel.get("images", {}).get("amenities", [])]
        )
        return Hotel(
            id=self.get_field(hotel, "id", "str"),
            destination_id=self.get_field(hotel, "destination", "int"),
            name=self.get_field(hotel, "name", "str"),
            location=location,
            description=self.get_field(hotel, "info", "str"),
            amenities=amenities,
            images=images,
            booking_conditions=[]
        )
        
        # testing
        # location = Location(
        #     lat=None,
        #     lng=None,
        #     address=None,
        #     city=None,
        #     country=None
        # )
        # amenities = Amenities(
        #     general=None,
        #     room=None,
        # )
        # images = Images(
        #     rooms=None,
        #     site=None,
        #     amenities=None
        # )
        # return Hotel(
        #     id=None,
        #     destination_id=None,
        #     name=None,
        #     location=location,
        #     description=None,
        #     amenities=amenities,
        #     images=images,
        #     booking_conditions=None
        # )

