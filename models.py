from dataclasses import dataclass
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


if __name__ == "__main__":
    mario_rossi = Client("Mario", "Rossi", "Via Milano 1, Torino (TO)", "RSSMRA85A01H501Z")
    line_item = LineItem("Wall painting", Decimal("80.00"), Decimal("34.50"))
    print(mario_rossi)
    print(line_item)