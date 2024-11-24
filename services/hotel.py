from models.hotel import Hotel

# filter hotels by id and destination
def filter_hotels(hotels, hotel_ids, destination_ids):
    if len(hotel_ids) == 0 or len(destination_ids) == 0:
      return hotels 

    return [
        hotel for hotel in hotels
        if hotel.id in hotel_ids and hotel.destination_id in destination_ids
    ]

# group hotels by hotel id and destination id
def group_by_hotel_and_destination(hotels):
    grouped_hotels = {}
    for hotel in hotels:
        key = (hotel.id, hotel.destination_id)
        if key not in grouped_hotels:
            grouped_hotels[key] = []
        grouped_hotels[key].append(hotel)
    
    # print(grouped_hotels)
    return grouped_hotels

def merge_two_hotels(merged_hotel: Hotel, hotel: Hotel) -> Hotel:
    merged_hotel.name = hotel.name if len(hotel.name) > len(merged_hotel.name) else merged_hotel.name
    merged_hotel.description = hotel.description if len(hotel.description) > len(merged_hotel.description) else merged_hotel.description
    merged_hotel.location.lat = hotel.location.lat if hotel.location.lat is not None else merged_hotel.location.lat
    merged_hotel.location.lng = hotel.location.lng if hotel.location.lng is not None else merged_hotel.location.lng
    merged_hotel.location.address = hotel.location.address if len(hotel.location.address) > len(merged_hotel.location.address) else merged_hotel.location.address
    merged_hotel.location.city = hotel.location.city if len(hotel.location.city) > len(merged_hotel.location.city) else merged_hotel.location.city
    merged_hotel.location.country = hotel.location.country if len(hotel.location.country) > len(merged_hotel.location.country) else merged_hotel.location.country
    merged_hotel.amenities.general = list(set(merged_hotel.amenities.general + hotel.amenities.general))
    merged_hotel.amenities.room = list(set(merged_hotel.amenities.room + hotel.amenities.room))
    merged_hotel.images.rooms.extend([img for img in hotel.images.rooms if img not in merged_hotel.images.rooms])
    merged_hotel.images.site.extend([img for img in hotel.images.site if img not in merged_hotel.images.site])
    merged_hotel.images.amenities.extend([img for img in hotel.images.amenities if img not in merged_hotel.images.amenities])
    merged_hotel.booking_conditions = list(set(merged_hotel.booking_conditions + hotel.booking_conditions))

# merge hotels with the same id and destination
def merge_hotel(hotels: list[Hotel]) -> Hotel:
    if not hotels:
        return None

    merged_hotel = hotels[0]
    for hotel in hotels[1:]:
        merge_two_hotels(merged_hotel, hotel)

    return merged_hotel