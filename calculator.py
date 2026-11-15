from decimal import Decimal, ROUND_HALF_UP

from loader import load_quote

# Money precision: 2 decimal places. Defined once, used by round_decimal().
CENT = Decimal("0.01")


def round_decimal(value):
    """Round a Decimal to 2 decimal places using ROUND_HALF_UP (0.125 -> 0.13)."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def calculate_subtotal(quote):
    """Return the sum of quantity * unit_price for every line item."""
    subtotal = Decimal("0")
    for item in quote.line_items:
        subtotal += item.unit_price * item.quantity
    return round_decimal(subtotal)


def calculate_discount(quote, subtotal):
    """Return the discount amount ("percent" or "fixed"); 0 if there is none."""
    if quote.discount_type == "percent":
        # discount_value is a percentage of the subtotal (e.g. 10 -> 10%)
        discount = subtotal * (quote.discount_value / Decimal("100"))
    elif quote.discount_type == "fixed":
        # discount_value is already an amount of money
        discount = quote.discount_value
    else:
        # No discount (discount_type is None or unknown)
        discount = Decimal("0")
    return round_decimal(discount)


def calculate_vat(quote, subtotal, discount):
    """Return the VAT amount, calculated on the discounted subtotal."""
    taxable = subtotal - discount
    return round_decimal(taxable * (quote.vat / Decimal("100")))


def total_amount(subtotal, discount, vat):
    """Return the final total: subtotal - discount + VAT."""
    return round_decimal(subtotal - discount + vat)


if __name__ == "__main__":
    # Quick manual test: runs only when this file is launched directly
    new_quote = load_quote("examples/quote.json")

    # The order matters: each step uses the results of the previous ones
    subtotal = calculate_subtotal(new_quote)
    discount = calculate_discount(new_quote, subtotal)
    vat = calculate_vat(new_quote, subtotal, discount)
    total = total_amount(subtotal, discount, vat)

    print(f"Subtotal: {subtotal} {new_quote.currency}")
    print(f"Discount: {discount} {new_quote.currency}")
    print(f"VAT: {vat} {new_quote.currency}")
    print(f"Total: {total} {new_quote.currency}")
