from dataclasses import asdict
import json
from typing import List

from models.hotel import Hotel


def string_to_array(string: str) -> List[str]:
    return string.split(",")

def arrstr_to_array(arrstr: List[str]) -> List[int]:
    if arrstr == ["none"]:
        return []
    return [int(x) for x in arrstr]

def print_hotel(hotels: List[Hotel]) -> None:
    with open("output.json", "w") as file:
        json.dump(hotels, file, default=lambda o: asdict(o), indent=4)