import json
import sys

from calculator import calculate_discount, calculate_subtotal, calculate_vat, total_amount
from errors import QuoteError
from loader import load_quote
from validate import validate_quote


if __name__ == "__main__":
    # Guard clause: argv[0] is the script name, so we need at least 2 items
    # (script + file path). Without it, argv[1] below would raise IndexError.
    if len(sys.argv) < 2:
        print("I need a correct path as an argument to load the quote.")
        sys.exit(1)

    try:
        # Order matters: load first, then validate, then calculate
        new_quote = load_quote(sys.argv[1])
        validate_quote(new_quote)

        # Each step uses the results of the previous ones
        subtotal = calculate_subtotal(new_quote)
        discount = calculate_discount(new_quote, subtotal)
        vat = calculate_vat(new_quote, subtotal, discount)
        total = total_amount(subtotal, discount, vat)

        print(f"Subtotal: {subtotal} {new_quote.currency}")
        print(f"Discount: {discount} {new_quote.currency}")
        print(f"VAT: {vat} {new_quote.currency}")
        print(f"Total: {total} {new_quote.currency}")
    # Python runs the first matching except; each one prints a readable message
    # and exits with code 1 (0 = success, anything else = error).
    except QuoteError as e:
        # Our own validation errors: the message is already user-friendly
        print(e)
        sys.exit(1)
    except FileNotFoundError:
        print(f"No such file or directory: {sys.argv[1]}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        # e holds the position of the problem (line and column)
        print(f"The file {sys.argv[1]} is not valid JSON: {e}")
        sys.exit(1)
