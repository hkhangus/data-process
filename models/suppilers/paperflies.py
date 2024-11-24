from models.hotel import Hotel, Location, Amenities, Images, Image
from models.suppilers.base import BaseSupplier

class PaperfliesSupplier(BaseSupplier):
    @property
    def url(self) -> str:
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"
    @property
    def name(self) -> str:
        return "paperflies"
    
    def parse(self, hotel: dict) -> Hotel:
        location = Location(
            lat=None,
            lng=None,
            address=self.get_field(hotel.get("location", {}), "address", "str"),
            city="",
            country=self.get_field(hotel.get("location", {}), "country", "str")
        )
        amenities = Amenities(
            general= self.get_field(hotel.get("amenities", {}), "general", "list"),
            room= self.get_field(hotel.get("amenities", {}), "room", "list")
        )
        images = Images(
            rooms = [Image(link=img["link"], description=img["caption"]) for img in self.get_field(hotel.get("images", {}), "rooms", "list")],
            site = [Image(link=img["link"], description=img["caption"]) for img in self.get_field(hotel.get("images", {}), "site", "list")]
        )
        return Hotel(
            id=self.get_field(hotel, "hotel_id", "str"),
            destination_id=self.get_field(hotel, "destination_id", "int"),
            name=self.get_field(hotel, "hotel_name", "str"),
            location=location,
            description=self.get_field(hotel, "details", "str"),
            amenities=amenities,
            images=images,
            booking_conditions=self.get_field(hotel, "booking_conditions", "list")
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