from typing import List, Dict
from abc import ABC, abstractmethod
import requests
import re

from models.hotel import Hotel

class BaseSupplier(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        pass
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    async def fetch_data(self): 
        try:
            response = requests.get(self.url, verify=False)
            return response.json()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def parse(hotel: Dict) -> Hotel:
        pass

    def get_field(self, hotel: Dict, field: str, type: str):
        case = {
            "str": lambda: (hotel.get(field, "") or "").strip(),
            "float": lambda: hotel.get(field) or None,
            "int": lambda: hotel.get(field) or None,
            "list": lambda: hotel.get(field, []) or []
        }
        return case[type]()
    
    def split_camel_case(self, amenity: str) -> str:
        if amenity.lower() == "wifi":
            return "wifi"
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', amenity).lower()