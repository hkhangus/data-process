import asyncio
import argparse
from models.suppilers.paperflies import PaperfliesSupplier
from models.suppilers.patagonia import PatagoniaSupplier
from utils.index import string_to_array, arrstr_to_array, print_hotel
from models.suppilers.acme import AcmeSupplier
from services.hotel import filter_hotels, group_by_hotel_and_destination, merge_hotel

async def main():
    # default config
    supplier_map = [AcmeSupplier(), PatagoniaSupplier(), PaperfliesSupplier()]

    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("hotel_ids", type=str, default="none", nargs="?")
    parser.add_argument("destination_ids", type=str, default="none", nargs="?")
    args = parser.parse_args()
    hotel_ids = string_to_array(args.hotel_ids)
    destination_ids = arrstr_to_array(string_to_array(args.destination_ids))
    print(hotel_ids)
    print(destination_ids)

    # fetch data
    raw_data = {}
    for supplier in supplier_map:
        print(f"Fetching data from {supplier.name}...")
        data = await supplier.fetch_data()
        if data:
            parsed_data = [supplier.parse(hotel) for hotel in data]
            # filter
            filtered_data = filter_hotels(parsed_data, hotel_ids, destination_ids)
            raw_data[supplier.name] = filtered_data

    # group
    hotels = [hotel for supplier_data in raw_data.values() for hotel in supplier_data]
    grouped_data = group_by_hotel_and_destination(hotels)

    # merge
    hotels = [merge_hotel(hotel_group) for hotel_group in grouped_data.values()]
    # hotels = [hotel for hotel_group in grouped_data.values() for hotel in hotel_group]
    print_hotel(hotels)
    print("Done, check output.json")

if __name__ == "__main__":
    asyncio.run(main())