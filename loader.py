from datetime import datetime
from decimal import Decimal
import json
from models import Client, LineItem, Quote


def load_quote(file_path):
    """Read a JSON file and return a Quote object."""
    # Read the file once; the data stays in memory after the file is closed
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    # Build the client from its nested dictionary
    client_data = data["client"]
    client = Client(
        name=client_data["name"],
        surname=client_data["surname"],
        address=client_data["address"],
        fiscal_code=client_data["fiscal_code"],
    )

    # Build one LineItem per entry; numbers arrive as strings, so convert to Decimal
    line_items = []
    for item in data["line_items"]:
        new_item = LineItem(
            description=item["description"],
            quantity=Decimal(item["quantity"]),
            unit_price=Decimal(item["unit_price"]),
        )
        line_items.append(new_item)

    # Convert VAT to Decimal and the date string (DD-MM-YYYY) to a date
    vat = Decimal(data["vat"])
    issue_date = datetime.strptime(data["issue_date"], "%d-%m-%Y").date()

    # Optional field: convert to Decimal only if it is present
    discount_value = data.get("discount_value")
    if discount_value is not None:
        discount_value = Decimal(discount_value)

    # .get() returns None (or the given default) when an optional key is missing
    quote = Quote(
        client=client,
        line_items=line_items,
        vat=vat,
        issue_date=issue_date,
        currency=data.get("currency", "EUR"),
        convert_currency=data.get("convert_currency"),
        discount_type=data.get("discount_type"),
        discount_value=discount_value,
    )

    return quote


if __name__ == "__main__":
    # Quick manual test: runs only when this file is launched directly
    quote = load_quote("examples/quote.json")
    print(quote)
