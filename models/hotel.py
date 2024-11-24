from dataclasses import dataclass, field, asdict
from typing import List

@dataclass
class Location:
    lat: float
    lng: float
    address: str
    city: str
    country: str

@dataclass
class Amenities:
    general: List[str]
    room: List[str]

@dataclass
class Image:
    link: str
    description: str

@dataclass
class Images:
    rooms: List[Image] = field(default_factory=list)
    site: List[Image] = field(default_factory=list)
    amenities: List[Image] = field(default_factory=list)

@dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    location: Location
    description: str
    amenities: Amenities
    images: Images
    booking_conditions: List[str] = field(default_factory=list)
    
    def get_data(self):
        return asdict(self)
