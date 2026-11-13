from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass
class Client:
    name: str
    surname: str
    address: str
    fiscal_code: str


@dataclass
class LineItem:
    description: str
    quantity: Decimal
    unit_price: Decimal


@dataclass
class Quote:
    # REQUIRED FIELDS
    client: Client
    line_items: list[LineItem]
    vat: Decimal
    issue_date: date

    # OPTIONAL FIELDS
    currency: str = "EUR"
    convert_currency: str | None = None
    discount_type: str | None = None
    discount_value: Decimal | None = None


if __name__ == "__main__":
    mario_rossi = Client("Mario", "Rossi", "Via Milano 1, Torino (TO)", "RSSMRA85A01H501Z")
    line_item = LineItem("Wall painting", Decimal("80.00"), Decimal("34.50"))
    new_quote = Quote(
        mario_rossi,
        [line_item],
        Decimal("22.00"),
        date(2026, 11, 13),
    )
    print(mario_rossi)
    print(line_item)
    print(new_quote)