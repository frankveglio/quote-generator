from errors import QuoteError
from loader import load_quote


def validate_quote(quote):
    """Check that the values in a Quote make sense; raise QuoteError if not."""
    # Guard clause: an empty list would skip the loop below and pass unnoticed,
    # so it is checked first. raise stops the function, no "else" needed.
    if not quote.line_items:
        raise QuoteError("The quote must contain at least one line item.")

    # enumerate(..., start=1) gives human line numbers: "Line 1", not "Line 0"
    for number, item in enumerate(quote.line_items, start=1):
        if item.quantity <= 0:
            raise QuoteError(f"Line {number}: quantity ({item.quantity}) must be a positive number.")
        # Price 0 is allowed (free items); only negative prices are rejected
        if item.unit_price < 0:
            raise QuoteError(f"Line {number}: unit_price ({item.unit_price}) must not be negative.")

    # Chained comparison: raise when VAT is NOT between 0 and 100
    if not 0 <= quote.vat <= 100:
        raise QuoteError(f"VAT ({quote.vat}) must be between 0 and 100.")


if __name__ == "__main__":
    # Quick manual test: runs only when this file is launched directly
    quote = load_quote("examples/wrong_quote.json")
    validate_quote(quote)
